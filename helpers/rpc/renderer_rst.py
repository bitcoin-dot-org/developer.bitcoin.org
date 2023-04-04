# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import os
import re
from collections import defaultdict
from pathlib import Path
import json

from help_data import display_name, capitalize, uncapitalize
from annotations import Annotations


class RendererRst:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.annotations = Annotations("annotations-bitcoin-0.21.json")

    def add_version_note(self, page):
        if "added" in self.annotation:
            page.text("*Added in Bitcoin Core %s*\n" %
                      self.annotation["added"])

    def add_wallet_note(self, page):
        if "wallet" in self.annotation:
            if self.annotation["wallet"]:
                page.text("*Requires wallet support.*\n")

    def add_see_also_command(self, page, command):
        name = display_name(command)
        lower_name = uncapitalize(name)
        page.text("* [%s][rpc %s]: {{summary_%s}}" %
                  (name, command, lower_name))

    def add_see_also_glossary(self, page, text, link):
        page.text("* [%s][/en/glossary/%s]" % (text, link))

    def add_see_also_message(self, page, message, text):
        page.text("* [`%s` message][%s message]: %s" %
                  (message, message, text))

    def add_see_also(self, page):
        if "see_also" in self.annotation:
            page.text("*See also*\n")
            see_also = self.annotation["see_also"]
            if "commands" in see_also:
                for command in see_also["commands"]:
                    self.add_see_also_command(page, command)
            if "glossary" in see_also:
                for glossary in see_also["glossary"]:
                    self.add_see_also_glossary(page, glossary[1], glossary[0])
            if "messages" in see_also:
                for message in see_also["messages"]:
                    self.add_see_also_message(page, message[0], message[1])
            page.nl()

    def arg_summary(self, arg):
        return arg["name"]

    def arg_n(self, arg):
        return arg["name"]

    def arg_t(self, arg):
        t = arg["type"].split(", ")[0]
        if t == "numeric":
            t = "number (int)"
        if "args" in self.annotation:
            args = self.annotation["args"]
            if arg["name"] in args:
                arg_annotation = args[arg["name"]]
                if "type" in arg_annotation:
                    t += " (%s)" % arg_annotation["type"]
        return t

    def arg_p(self, arg):
        arg_line = arg["type"].split(", ")
        if len(arg_line) == 1:
            return "Required"
        else:
            p = arg_line[1]
            if p == "required":
                return "Required<br>(exactly 1)"
            elif p == "optional":
                if len(arg_line) == 3:
                    return "Optional<br>" + capitalize(arg_line[2])
                else:
                    return "Optional"
            else:
                return p

    def arg_d(self, arg):
        d = arg["description"]
        if "args" in self.annotation:
            args = self.annotation["args"]
            if arg["name"] in args:
                arg_annotation = args[arg["name"]]
                if "description" in arg_annotation:
                    d += ". " + arg_annotation["description"]
        return d

    def result_t(self, result):
        t = result["type"]
        if t == "numeric":
            t = "number (int)"
        elif t == "string":
            t += " (hex)"
        return t

    def result_null(self):
        return '''*Result---`null` on success*

{% itemplate ntpd1 %}
- n: "`result`"
  t: "null"
  p: "Required<br>(exactly 1)"
  d: "JSON `null` when the command was successfull or a JSON with an error field on error."

{% enditemplate %}
'''

    def yaml_escape(self, text):
        return text.replace('"', '\\"')

    def guarded_code_block(self, block):
        return "{% endautocrossref %}\n\n" + self.code_block(block) + "\n{% autocrossref %}\n"

    def code_block(self, block):
        min_indentation = 999
        split_block = block.splitlines()
        for line in split_block:
            indentation = len(line) - len(line.lstrip(" "))
            if indentation < min_indentation:
                min_indentation = indentation

        indented_block = ""
        for line in split_block:
            if min_indentation <= 4:
                indented_block += " " * (4 - min_indentation) + line
            else:
                indented_block += line[min_indentation - 4:]
            indented_block += "\n"
        if not indented_block.endswith("\n"):
            indented_block += "\n"
        return indented_block

    def license_header(self):
        output = ""
        output += ".. This file is licensed under the MIT License (MIT) available on\n"
        output += "   http://opensource.org/licenses/MIT.\n\n"
        return output

    def table(self, rows, title=None):
        output = '.. list-table::'
        if title:
            output += ' ' + title
        output += '\n   :header-rows: 1\n\n'
        output += '   * - Name\n     - Type\n     - Description\n'
        for row in rows:
            output += '   * - ' + row["name"] + '\n'
            output += '     - ' + row["type"] + '\n'
            if row["description"]:
                description = row["description"]
            else:
                description = "object"
            output += '     - ' + description + '\n'
        return output

    def cmd_page(self, help_data):
        output = ""
        output += self.license_header()
        output += self.title(help_data["command"].split(" ")[0])
        output += "\n"
        output += '``' + help_data["command"] + '``\n\n'
        output += help_data['description'].replace("*", r"\*") + '\n'
        if help_data['arguments']:
            number = 1
            for argument in help_data['arguments']:
                title = 'Argument #' + str(number) + ' - ' + argument['name']
                output += title + '\n'
                output += '~' * len(title) + '\n\n'
                output += '**Type:** ' + argument['type'] + '\n\n'
                if argument['description']:
                    output += argument['description'] + '\n\n'
                if 'literal_description' in argument:
                    output += '::\n\n' + argument['literal_description'] + '\n'
                number += 1
        if help_data['results']:
            for result in help_data['results']:
                if result and 'format' in result:
                    if result['format'] == 'table':
                        full_title = "Result"
                        if 'title_extension' in result:
                            full_title += result['title_extension']
                        output += full_title + '\n'
                        output += '~' * len(full_title) + '\n\n'
                        output += self.table([result]) + '\n'
                    elif result['format'] == 'literal':
                        result_title = 'Result'
                        if 'title_extension' in result:
                            result_title += result['title_extension']
                        output += result_title + '\n' + '~' * \
                            len(result_title) + '\n\n::\n\n' + \
                            result['text'] + '\n'
        if help_data["examples"]:
            output += 'Examples\n~~~~~~~~\n\n'
            output += '\n.. highlight:: shell\n\n'
            text = ''
            for example_line in help_data['examples']:
                if example_line.startswith('> '):
                    output += text + '::\n\n'
                    output += '  ' + example_line[2:].rstrip() + '\n\n'
                    text = ''
                else:
                    text += example_line
        return output

    def render_cmd_page(self, command, help_data):
        command_file = command + ".rst"
        with open(str(self.output_dir / command_file), "w") as cmd_file:
            cmd_file.write(self.cmd_page(help_data))

    def title(self, text, level=0):
        underline_symbol = "=-~^"[level]
        return text + "\n" + len(text) * underline_symbol + "\n"

    def index_page(self, all_commands):
        output = ""

        output += self.title("RPC API Reference")
        output += "\n"

        for category in sorted(all_commands):
            output += self.title(category + " RPCs", level=1)
            output += "\n"
            if category == "Wallet":
                output += """**Note:** the wallet RPCs are only available if Bitcoin Core was built
with wallet support, which is the default.

"""
            output += ".. toctree::\n"
            output += "  :maxdepth: 1\n\n"
            for command in all_commands[category]:
                cmd = command.split(" ")[0]
                output += "  " + cmd + "\n"
            output += "\n"

        return output

    def render_overview_page(self, all_commands, render_version_info=True):
        with open(str(self.output_dir / "index.rst"), "w") as index_file:
            output = ""
            output += self.license_header()
            output += self.index_page(all_commands)
            index_file.write(output)
