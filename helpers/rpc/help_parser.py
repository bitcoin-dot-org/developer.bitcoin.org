# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import re
from enum import Enum
from collections import defaultdict


class CommandList:
    def __init__(self):
        self.commands_by_group = defaultdict(list)

    def add(self, group, command):
        self.commands_by_group[group].append(command)

    def grouped(self):
        return self.commands_by_group

    def flat(self):
        commands = []
        for group in self.commands_by_group:
            for command in self.commands_by_group[group]:
                commands.append(command.split(" ")[0])
        return sorted(commands)


class HelpParser:
    '''A parser for the Bitcoin Core RPC command line help'''

    Section = Enum(
        'Section', 'command description result literal_result past_result '
                   'arguments literal_argument examples')

    def __init__(self):
        self.json_level = 0

    def parse_help_result(self, result_line):
        match = re.match(r'([^\s]*)\s+\((.*)\)\s+(.*)', result_line)
        if match:
            name = match.group(1)
            if name[0] == '"' and name[-1] == '"':
                name = name[1:-1]
            return {'format': 'table', 'name': name, "type": match.group(2),
                    "description": match.group(3)}
        else:
            return None

    def parse_help_argument(self, result_line):
        match = re.match(r'\d\.\s+([^\s]*)\s+\((.*?)\)\s*(.*)', result_line)
        if match:
            name = match.group(1)
            if name[0] == '"' and name[-1] == '"':
                name = name[1:-1]
            return {"name": name, "type": match.group(2),
                    "description": match.group(3)}
        else:
            return None

    def next_section(self, line, help_data):
        """Check line for section identifiers and move state to next section if
        found. Returns if a new section was found and the state was changed.
        """
        previous_section = self.section
        result_match = re.match(r'^Result:?([^:]*):?$', line)
        if result_match and (':' in line or line == 'Result' or line.startswith('Result (')):
            self.section = self.Section.result
            help_data['results'].append(
                {'title_extension': result_match.group(1)})
        elif line == "Arguments:":
            self.section = self.Section.arguments
        elif re.match(r'Examples?:', line):
            self.section = self.Section.examples
        return previous_section != self.section

    def check_opening_json(self, line):
        """Checks line for brackets opening a JSON object and sets the
        json_level accordingly. Detects one-line JSON which is closed in the
        same line.
        """
        if line.endswith('},') or line.endswith('],'):
            line = line[:-1]
        match = re.match(r"^ *([\[{])", line)
        if match:
            pairs = [
                ['{', '}'],
                ['[', ']'],
            ]
            for pair in pairs:
                if match.group(1) == pair[0] and (line[-len(pair[1]):] != pair[1]):
                    self.json_level += 1
                    return

    def parse_help_overview(self, help_text):
        command_list = CommandList()
        group = ""
        for line in help_text.splitlines():
            pattern = re.compile("== (.*) ==")
            match = pattern.match(line)
            if match:
                group = match.group(1)
            else:
                if len(line) > 0:
                    command_list.add(group, line.rstrip())
        return command_list

    def parse_help_command(self, help_text):
        self.section = self.Section.command
        self.literal_description = False
        help_data = {
            "command": "",
            "description": "",
            "results": [],
            "arguments": [],
            "examples": [],
        }
        for line in help_text.splitlines():
            # print("LINE (" + self.section.name + ") " + line)

            if self.section == self.Section.command:
                help_data['command'] = line.rstrip()
                self.section = self.Section.description

            elif self.section == self.Section.description:
                if not self.next_section(line, help_data):
                    if line:
                        if line.startswith(" "):
                            self.literal_description = True
                        else:
                            if self.literal_description:
                                help_data["description"] += '\n'
                                self.literal_description = False
                        if help_data["description"] and help_data["description"][-2] in ['.', ':']:
                            help_data["description"] += '\n'
                        help_data["description"] += line.rstrip() + '\n'

            elif self.section == self.Section.arguments:
                if not self.next_section(line, help_data):
                    if line:
                        argument = self.parse_help_argument(line)
                        if argument:
                            help_data["arguments"].append(argument)
                        else:
                            if help_data['arguments']:
                                last_argument = help_data["arguments"][-1]
                                if last_argument:
                                    self.check_opening_json(line)
                                    if self.json_level > 0:
                                        last_argument['literal_description'] = line + '\n'
                                        self.section = self.Section.literal_argument
                                    else:
                                        if line.startswith(' '):
                                            if last_argument['description']:
                                                last_argument['description'] += '\n       '
                                            last_argument['description'] += line.lstrip()

            elif self.section == self.Section.literal_argument:
                last_argument = help_data['arguments'][-1]
                last_argument['literal_description'] += line + '\n'
                self.check_opening_json(line)
                if re.match(r"^ *[\]}]", line):
                    self.json_level -= 1
                    if self.json_level == 0:
                        self.section = self.Section.arguments

            elif self.section == self.Section.result:
                if not self.next_section(line, help_data):
                    if line.startswith("{") or (line.startswith("[") and not "]" in line):
                        self.section = self.Section.literal_result
                        result_data = help_data['results'][-1]
                        result_data.update(
                            {'format': 'literal', 'text': '  ' + line + '\n'})
                    else:
                        if line and not line.startswith(" "):
                            result_data_line = self.parse_help_result(line)
                            result_data = help_data['results'][-1]
                            if result_data_line:
                                result_data.update(result_data_line)
                            else:
                                result_data.update(
                                    {'format': 'literal', 'text': '  ' + line + '\n'})
                            self.section = self.Section.past_result

            elif self.section == self.Section.literal_result:
                last_result = help_data['results'][-1]
                last_result['text'] += '  ' + line.rstrip() + '\n'
                if line == "}" or line == ']':
                    self.section = self.Section.past_result

            elif self.section == self.Section.past_result:
                self.next_section(line, help_data)

            elif self.section == self.Section.examples:
                if line:
                    help_data["examples"].append(line)

        self.fixup(help_data)
        return help_data

    def fixup(self, help_data):
        command = help_data["command"].split(" ")[0]
        if command == "getblock" or command == "getblockheader":
            help_data["description"] = help_data["description"].replace("<hash>", "'hash'")
