# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.
from pathlib import Path
import os

from help_parser import HelpParser, CommandList

test_data_dir = Path(os.path.dirname(__file__)) / "test_data"


def test_parse_help():
    with open(str(test_data_dir / "examplecommand")) as file:
        input = file.read()
    result = HelpParser().parse_help_command(input)
    assert result["command"] == 'examplecommand "arg" "object" ( "optional-arg" )'
    assert result["description"] == "Returns something.\n"
    assert len(result["arguments"]) == 7
    assert result["arguments"][0] == {
        'name': 'arg', 'type': 'string, required',
        'description': 'An argument.'}
    assert result["arguments"][1] == {
        'name': 'otherarg', 'type': 'string, required',
        'description': 'Line one\n       line two'}
    assert result["arguments"][2] == {
        'name': 'object',
        'type': 'array, required',
        'description': 'Some data',
        'literal_description': '  [     (array of json objects)\n'
        '    {\n'
        '      "key": "value", (type) desc\n'
        '    }\n'
        '  ,...\n'
        '  ]\n',
    }
    assert result["arguments"][3] == {
        'name': 'optional-arg', 'type': 'string, optional',
        'description': 'An optional argument.'}
    assert result["arguments"][4] == {
        'name': 'options',
        'type': 'json, optional',
        'description': '',
        'literal_description': '  {\n'
        '     "rescan": <false>, (xx) yy\n'
        '  }\n',
    }
    assert result["arguments"][5] == {
        'name': 'inputs',
        'type': 'array',
        'description': 'A json array',
        'literal_description': '     [\n'
        '       {\n'
        '         "txid":"id",    (s) id\n'
        '                             [vout_index,...]\n'
        '       }\n'
        '       ,...\n'
        '     ]\n',
    }
    assert result["arguments"][6] == {
        'name': 'outputs',
        'type': 'object',
        'description': 'a json object',
        'literal_description': '    {\n'
        '      "address": x.xxx,    (ns) a\n'
        '      "data": "hex"      (s) data\n'
        '      ,...\n'
        '    }\n',
    }
    assert result["results"] == [{'format': 'table', 'title_extension': '',
                                  'name': "hex", "type": "string",
                                  "description": "the result, hex encoded"}]
    assert result["examples"] == ["> bitcoin-cli examplecommand foo",
                                  "> curl --user myusername --data-binary someargs"]


def test_parse_help_result_with_quotes():
    assert HelpParser().parse_help_result('"hex"      (string) some thing') == {
        'format': 'table', 'name': 'hex', 'type': 'string', 'description': 'some thing'}


def test_parse_help_result_without_quotes():
    assert HelpParser().parse_help_result('hex      (string) some thing') == {
        'format': 'table', 'name': 'hex', 'type': 'string', 'description': 'some thing'}


def test_parse_help_argument_with_quotes():
    assert HelpParser().parse_help_argument('1. "inputs" (hex, required) some arg.') == {
        'name': 'inputs', 'type': 'hex, required', 'description': 'some arg.'}


def test_parse_help_argument_without_quotes():
    assert HelpParser().parse_help_argument('1. inputs (hex, required) some arg.') == {
        'name': 'inputs', 'type': 'hex, required', 'description': 'some arg.'}


def test_parse_help_arguments_without_description():
    assert HelpParser().parse_help_argument('2. options               (object, optional)') == {
        'name': 'options', 'type': 'object, optional', 'description': ''}


def test_check_and_set_json_level():
    parser = HelpParser()

    def check(line, expected_json_level):
        parser.check_opening_json(line)
        assert parser.json_level == expected_json_level

    check(' x', 0)
    check(' {', 1)
    check(' [', 2)
    check(' []', 2)
    check(' {}', 2)
    check(' {},', 2)
    check(' [],', 2)


def test_command_list():
    cmds = CommandList()
    cmds.add("group1", "cmd1")
    cmds.add("group1", "cmd2 arg")
    cmds.add("group2", "anothercmd")
    assert cmds.grouped() == {
        "group1": ["cmd1", "cmd2 arg"],
        "group2": ["anothercmd"]
    }
    assert cmds.flat() == ["anothercmd", "cmd1", "cmd2"]
