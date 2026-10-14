# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.
from help_parser import HelpParser
from cli_caller import CliCaller

# RPCs that exist but are omitted from `bitcoin-cli help` (hidden since
# Bitcoin Core 30). They still answer `help <cmd>`, so they can be documented.
HIDDEN_COMMANDS = {
    "Generating": ["generateblock", "generatetoaddress",
                   "generatetodescriptor"],
}


class Generator:
    def __init__(self, cli, renderer):
        self.cli = CliCaller(cli)
        self.renderer = renderer

    def generate_command(self, command):
        print("Command %s" % command)
        command_output = self.cli.help(command)
        help_data = HelpParser().parse_help_command(command_output)
        self.renderer.render_cmd_page(command, help_data)

    def generate_overview(self):
        help_output = self.cli.help()
        command_list = HelpParser().parse_help_overview(help_output)

        listed = command_list.flat()
        for group, names in HIDDEN_COMMANDS.items():
            for name in names:
                if name not in listed:
                    command_list.add(group, name)

        self.renderer.render_overview_page(command_list.grouped(),
                                           render_version_info=False)

        count = 1
        for command in command_list.flat():
            self.generate_command(command)
            count += 1

        print("Generated pages for %s commands." % count)
