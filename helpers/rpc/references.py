# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from pathlib import Path

from help_data import display_name

class References:
    def __init__(self, docs_dir):
        self.docs_dir = Path(docs_dir)

    def anchor(self, command):
        if command == "ping":
            return "ping-rpc"
        else:
            return command

    def update(self, commands):
        self.update_references(commands)
        self.update_autocrossref(commands)
        self.update_config(commands)
        self.update_api_intro(commands)

    def update_file(self, commands, path, start_marker, content_call,
                    replace_start_marker=False, end_marker=None):
        file_path = self.docs_dir / path
        print("Updating file %s ..." % file_path)
        output = ""
        with file_path.open() as ref_file:
            skip_lines = False
            for line in ref_file:
                if skip_lines:
                    if (end_marker and end_marker in line) or (not end_marker and line == "\n"):
                        skip_lines = False
                        output += line
                else:
                    if start_marker in line:
                        if not replace_start_marker:
                            output += line
                        skip_lines = True
                        for command in commands:
                            output += content_call(command) + "\n"
                    else:
                        output += line

        with file_path.open("w") as f:
            f.write(output)

    def update_references(self, commands):
        self.update_file(commands, Path("_includes", "references.md"), "<!-- RPCs",
                lambda command : "[rpc %s]: /en/developer-reference#%s" % (command, self.anchor(command)))

    def update_autocrossref(self, commands):
        self.update_file(commands, Path("_autocrossref.yaml"), "## RPCs",
                lambda command : (("'`%s`': rpc %s\n" % (command, command)) +
                                  ("'`%s` RPC': rpc %s") % (command, command)))

    def update_config(self, commands):
        self.update_file(commands, Path("_config.yml"), '  "RPCs":',
                lambda command : ("    - '%s': \"/en/developer-reference#%s\"" %
                                  (display_name(command), self.anchor(command))))

    def update_api_intro(self, commands):
        self.update_file(commands, Path("_data/devdocs/en/bitcoin-core/api-intro.md"), "/bitcoin-core/rpcs/rpcs/",
                lambda command : "{%% include_absolute _data/devdocs/{{page.lang}}/bitcoin-core/rpcs/rpcs/%s.md " \
                                 "_data/devdocs/en/bitcoin-core/rpcs/rpcs/%s.md %%}\n" % (command, command),
                replace_start_marker=True, end_marker="/bitcoin-core/rest/")
