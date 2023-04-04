# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from renderer_rst import RendererRst
from help_parser import HelpParser
from pathlib import Path
import os

test_data_dir = Path(os.path.dirname(__file__)) / "test_data"


def test_process_command_help():
    cmds = [
        'analyzepsbt',
        'deriveaddresses',
        'getblockstats',
    ]
    for cmd in cmds:
        with open(str(test_data_dir / cmd)) as file:
            input = file.read()
            help_data = HelpParser().parse_help_command(input)
        with open(str(test_data_dir / "rst" / (cmd + ".rst"))) as file:
            expected_output = file.read()
        assert RendererRst("").cmd_page(
            help_data) == expected_output
