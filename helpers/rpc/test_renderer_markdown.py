# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.
from renderer_markdown import RendererMarkdown
from help_parser import HelpParser
from pathlib import Path
import os

test_data_dir = Path(os.path.dirname(__file__)) / "test_data"


def test_process_command_help():
    cmds = [
        'abandontransaction',
        'addmultisigaddress',
        'addnode',
        'getbestblockhash',
        'getblock',
        'gettxoutproof',
        'pruneblockchain',
        'getmemoryinfo',
        'analyzepsbt',
        'deriveaddresses',
        'ping',
    ]
    for cmd in cmds:
        with open(str(test_data_dir / cmd)) as file:
            input = file.read()
            help_data = HelpParser().parse_help_command(input)
        with open(str(test_data_dir / "markdown" / (cmd + ".md"))) as file:
            expected_output = file.read()
        assert RendererMarkdown("").process_command_help(
            help_data) == expected_output


def test_code_block():
    r = RendererMarkdown("")

    assert r.code_block("abc") == "    abc\n"
    assert r.code_block("  def") == "    def\n"
    assert r.code_block("     xxx\n     yyy") == "    xxx\n    yyy\n"
    assert r.code_block("  {\n    x\n  }\n") == "    {\n      x\n    }\n"
    assert r.code_block(
        "      {\n        x\n      }\n") == "    {\n      x\n    }\n"


def test_yaml_escape():
    r = RendererMarkdown("")

    assert r.yaml_escape('a "string"') == 'a \\"string\\"'


def test_split_description():
    r = RendererMarkdown("")
    r.annotation = {}

    summary, description = r.split_description("One line\n")
    assert summary == "one line."
    assert description == ""

    summary, description = r.split_description("One line.")
    assert summary == "one line."
    assert description == ""

    summary, description = r.split_description("First line\nsecond line\n")
    print(summary)
    assert summary == "first line second line."
    assert description == ""

    summary, description = r.split_description("First\nsecond. Third.\n")
    print(summary)
    assert summary == "first second."
    assert description == "Third.\n"
