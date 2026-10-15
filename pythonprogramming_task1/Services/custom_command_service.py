import json
import webbrowser
from pathlib import Path


class CustomCommandService:

    def __init__(self, command_file: str):
        self.command_file = Path(command_file)
        self.commands = self._load_commands()

    def _load_commands(self) -> dict:
        if not self.command_file.exists():
            return {}

        with open(
            self.command_file,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    def find_command(self, command: str):
        command = command.lower().strip()

        return self.commands.get(command)

    def execute(self, command_data: dict) -> str:
        action = command_data.get("action")
        value = command_data.get("value")

        if action == "open_url":
            webbrowser.open(value)
            return "Opening it now."

        return "That custom command is not supported yet."
