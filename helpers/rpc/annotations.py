# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

import json
from pathlib import Path
import os
import re

from cli_caller import CliCaller
from help_parser import HelpParser


class Annotations:
    def __init__(self, filename):
        self.filename = filename
        self.load()

    def load(self):
        with open(self.filename) as file:
            self.annotations = json.load(file)

    def save(self):
        with open(self.filename, "w") as file:
            file.write(json.dumps(self.annotations, indent=2, sort_keys=True))

    def annotation(self, command):
        if command in self.annotations:
            return self.annotations[command]
        else:
            return {}

    def import_see_also(self, dir):
        with open(self.filename) as file:
            annotations = json.load(file)
        for filename in os.listdir(dir):
            command = filename.partition(".")[0]
            print(command)
            see_also_commands = []
            with open(Path(dir) / filename) as file:
                found_see_also = False
                for line in file:
                    if line.startswith("*See also*"):
                        found_see_also = True
                        continue
                    if found_see_also and line.startswith("* "):
                        match = re.match(r"^\* .*\[rpc (.*)\]", line)
                        if match:
                            print("  ", match.group(1))
                            see_also_commands.append(match.group(1))
            if see_also_commands:
                if not command in annotations:
                    annotations[command] = {}
                commands = {
                    "commands": see_also_commands
                }
                if "see_also" in annotations[command]:
                    annotations[command]["see_also"].update(commands)
                else:
                    annotations[command]["see_also"] = commands
        with open(self.filename, "w") as file:
            file.write(json.dumps(annotations, indent=2, sort_keys=True))

    def clean_annotations(self):
        self.load()

        to_be_cleaned = []
        removed_commands = []
        for command in self.annotations:
            annotation = self.annotations[command]
            if "see_also" in annotation:
                if annotation["see_also"] == {"commands": [""]}:
                    annotation.pop("see_also")
            if annotation == {}:
                to_be_cleaned.append(command)
            if "removed" in annotation:
                removed_commands.append(command)

        for command in to_be_cleaned:
            self.annotations.pop(command)

        for command in self.annotations:
            annotation = self.annotations[command]
            if "see_also" in annotation:
                if "commands" in annotation["see_also"]:
                    commands = annotation["see_also"]["commands"]
                    for removed_command in removed_commands:
                        if removed_command in commands:
                            commands.remove(removed_command)
                    if not commands:
                        annotation["see_also"].pop("commands")
                    if not annotation["see_also"]:
                        annotation.pop("see_also")

        self.save()

    def mark_removed(self, version, command):
        self.load()
        if not command in self.annotations:
            self.annotations[command] = {}
        annotation = self.annotations[command]
        annotation["removed"] = version
        if "see_also" in annotation:
            annotation.pop("see_also")
        self.save()

    def mark_added(self, version, command):
        self.load()
        if not command in self.annotations:
            self.annotations[command] = {}
        annotation = self.annotations[command]
        annotation["added"] = version
        self.save()

    def show_missing(self, commands):
        self.load()
        for command in commands:
            if not command in self.annotations:
                print(command)
