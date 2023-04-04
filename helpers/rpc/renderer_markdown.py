# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import os
import re
from collections import defaultdict
from pathlib import Path
import json

from help_data import display_name, capitalize, uncapitalize
from annotations import Annotations


class Tag:
    def __init__(self, doc, name):
        self.doc = doc
        self.name = name

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        self.doc.out += "{%% end%s %%}\n" % self.name


class Page:
    def __init__(self):
        self.out = ""

    def tag(self, name, arg=None):
        self.out += "{%% %s " % name
        if arg:
            self.out += arg + " "
        self.out += "%}\n"
        return Tag(self, name)

    def text(self, text):
        self.out += text + "\n"

    def nl(self):
        self.text("")


class RendererMarkdown:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.annotations = Annotations("annotations-bitcoin-0.18.json")

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

    def add_license_header(self, page):
        with page.tag("comment"):
            page.text("This file is licensed under the MIT License (MIT) available on\n"
                      "http://opensource.org/licenses/MIT.")

    def split_description(self, full_description):
        if "summary" in self.annotation:
            summary = self.annotation["summary"]
            description = full_description
        elif full_description:
            if "." in full_description:
                summary = uncapitalize(full_description.partition(".")[0]) + "."
                description = full_description[len(summary) + 1:].lstrip()
            else:
                summary = uncapitalize(full_description.rstrip()) + "."
                description = ""
            summary = " ".join(summary.splitlines())
        else:
            summary = "does %s." % display_name(self.command)
            description = None
        return summary, description

    def process_command_help(self, help_data):
        self.help_data = help_data
        # print(help_data)
        self.command = help_data["command"].split(" ")[0]
        self.annotation = self.annotations.annotation(self.command)

        page = Page()

        self.add_license_header(page)

        name = display_name(self.command)
        lower_name = name[0].lower() + name[1:]

        page.tag(
            "assign", 'filename="_data/devdocs/en/bitcoin-core/rpcs/rpcs/%s.md"' % self.command)
        title = "\n##### %s" % name
        if self.command == "ping":
            title += " {#ping-rpc}"
            suffix = "-rpc"
        else:
            suffix = ""
        page.text(title)
        page.tag("include", "helpers/subhead-links.md")
        page.nl()
        summary, description = self.split_description(help_data["description"])
        page.tag("assign", 'summary_%s%s="%s"' % (lower_name, suffix, summary))
        page.nl()
        with page.tag("autocrossref"):
            page.nl()
            self.add_version_note(page)
            self.add_wallet_note(page)
            page.text("The `%s` RPC {{summary_%s%s}}\n" %
                      (self.command, lower_name, suffix))
            if description:
                quoted = False
                for line in description.splitlines():
                    if line.startswith("    "):
                        if not quoted:
                            page.text("{% endautocrossref %}")
                            page.nl()
                            quoted = True
                    elif quoted:
                        page.nl()
                        page.text("{% autocrossref %}")
                        quoted = False
                    page.text(line)
                if quoted:
                    page.nl()
                    page.text("{% autocrossref %}")
                page.nl()

            if "arguments" in help_data:
                if not help_data["arguments"]:
                    page.text("*Parameters: none*\n")
                else:
                    count = 1
                    for arg in help_data["arguments"]:
                        page.text("*Parameter #%s---%s*\n" %
                                  (count, self.arg_summary(arg)))
                        with page.tag("itemplate", "ntpd1"):
                            page.text('- n: "%s"' % self.arg_n(arg))
                            page.text('  t: "%s"' % self.arg_t(arg))
                            page.text('  p: "%s"' %
                                      self.yaml_escape(self.arg_p(arg)))
                            page.text('  d: "%s"' %
                                      self.yaml_escape(self.arg_d(arg)))
                            page.nl()
                        page.nl()
                        if "literal_description" in arg:
                            page.text(self.guarded_code_block(
                                arg["literal_description"]))

                        count += 1

            if help_data["results"] == [{'title_extension': ''}] or help_data["results"] == []:
                page.text(self.result_null())
            else:
                for result in help_data["results"]:
                    result_header = "*Result"
                    if "title_extension" in result and result["title_extension"]:
                        result_header += "---" + \
                            result["title_extension"].lstrip()
                    result_header += "*\n"
                    page.text(result_header)
                    if result["format"] == "literal":
                        page.text(self.guarded_code_block(result["text"]))
                    else:
                        with page.tag("itemplate", "ntpd1"):
                            page.text('- n: "%s"' % "`result`")
                            page.text('  t: "%s"' % self.result_t(result))
                            page.text('  p: "Required<br>(exactly 1)"')
                            page.text('  d: "%s"' %
                                      self.yaml_escape(result["description"]))
                            page.nl()
                        page.nl()

            if help_data["examples"]:
                page.text("*Example*\n")
                for example in help_data["examples"]:
                    if example.startswith("> "):
                        if not example.startswith("> curl"):
                            with page.tag("highlight", "bash"):
                                page.text(example[2:].rstrip())
                    else:
                        if (not example.startswith("As json rpc") and
                            not example.startswith("As a json rpc") and
                            not example.startswith("As a JSON-RPC")):
                            page.text(example)
                            page.nl()
                page.nl()

            self.add_see_also(page)

        return page.out

    def render_cmd_page(self, command, help_data):
        command_file = command + ".md"
        with open(self.output_dir / "rpcs" / command_file, "w") as file:
            file.write(self.process_command_help(help_data))

    def add_version_helper_assignment(self, page, type, version, bold=False):
        a = type.upper() + version.replace(".", "_") + "='*"
        if bold:
            a += "*"
        a += '<abbr title="' + type + ' in Bitcoin Core v' + version + '">'
        a += type + ' in ' + version + '</abbr>*'
        if bold:
            a += "*"
        a += "'"
        page.tag("assign", a)

    def add_version_helpers(self, page, version, date, new=False, updated=True, bold=False):
        page.text("<!-- Bitcoin Core %s %s -->" % (version, date))
        if new:
            self.add_version_helper_assignment(page, "New", version, bold=bold)
        if updated:
            self.add_version_helper_assignment(
                page, "Updated", version, bold=bold)
        page.nl()

    def render_version_info(self, page):
        with page.tag("comment"):
            page.text("""Styling notes: use highly-visible style for upcoming changes (not yet
released) and changes made in the last 6 months.  Use less-visible
style for changes made up to two years ago.  Don't point out
changes made more than two years ago.

Use v0.n.n in abbreviation title to prevent autocrossrefing.""")
        page.nl()
        page.text("<!-- Deprecated -->")
        page.tag("assign", "DEPRECATED='**<abbr title=\"Deprecated; will be removed in a future version of Bitcoin Core\">Deprecated</abbr>**'")

        self.add_version_helpers(page, "0.14.1", "April 2017", bold=True)
        self.add_version_helpers(
            page, "0.14.0", "March 2017", new=True, bold=True)
        self.add_version_helpers(page, "0.13.1", "September 2016")
        self.add_version_helpers(page, "0.13.0", "August 2016", new=True)
        self.add_version_helpers(page, "0.12.1", "April 2016")
        self.add_version_helpers(page, "0.12.0", "February 2016", new=True)
        self.add_version_helpers(
            page, "0.11.0", "July 2015", new=True, updated=False)

    def render_overview_page(self, all_commands, render_version_info=True):
        with open(self.output_dir / "quick-reference.md", "w") as file:
            page = Page()

            self.add_license_header(page)
            page.tag(
                "assign", 'filename="_data/devdocs/en/bitcoin-core/rpcs/quick-reference.md"')
            page.nl()
            page.text("#### Quick Reference {#rpc-quick-reference}")
            page.tag("include", "helpers/subhead-links.md")
            page.nl()

            if render_version_info:
                self.render_version_info(page)

            page.text("""<!-- the summaries used below are defined in the files for the
     particular RPC and aggregated into this helper file by the makefile
     function manual-update-summaries-file. For example, to edit the
     summary for GetBestBlockHash, edit
     _includes/rpc/getbestblockhash.md and run `make manual-update-summaries`. -->""")
            page.tag("include", "helpers/summaries.md")
            page.nl()

            for category in all_commands:
                page.text("#### " + category + " RPCs")
                page.text("{:.no_toc}")
                page.text("<!-- no subhead-links here -->\n")
                with page.tag("autocrossref"):
                    page.nl()
                    if category == "Wallet":
                        page.text("""**Note:** the wallet RPCs are only available if Bitcoin Core was built
with [wallet support][]{:#term-wallet-support}{:.term}, which is the
default.
""")
                    for command in all_commands[category]:
                        cmd = command.split(" ")[0]
                        item = "* [" + display_name(cmd) + "]"
                        item += "[rpc " + cmd + "]: "
                        item += "{{summary_" + uncapitalize(display_name(cmd))
                        if cmd == "ping":
                            item += "-rpc"
                        item += "}}"
                        if render_version_info:
                            annotation = self.annotations.annotation(cmd)
                            if "added" in annotation:
                                item += " {{NEW%s}}" % annotation["added"].replace(
                                    ".", "_")
                            if "added" in annotation and "changed" in annotation:
                                item += ","
                            if "changed" in annotation:
                                item += " {{UPDATED%s}}" % annotation["changed"].replace(
                                    ".", "_")
                            if "deprecated" in annotation:
                                item += " {{DEPRECATED}}"
                        page.text(item)
                    page.nl()
                page.nl()

            file.write(page.out)
