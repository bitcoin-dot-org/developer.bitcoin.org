# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import subprocess


class CliCaller:
    def __init__(self, cli):
        self.cli = cli

    def help(self, cmd=None):
        arg = ["help"]
        if cmd:
            arg.append(cmd)
        result = subprocess.check_output([str(self.cli.cli_path)] + self.cli.cli_args +
                                arg)
        return result.rstrip().decode("utf-8")
