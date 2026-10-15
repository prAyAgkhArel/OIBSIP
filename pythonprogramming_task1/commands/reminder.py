import re


class ReminderCommand:

    def __init__(self, reminder_service):
        self.reminder_service = reminder_service

    def execute(self, command: str) -> str:
        parsed = self.parse_reminder(command)

        if parsed is None:
            return (
                "Please say something like, "
                "remind me in 10 minutes to study."
            )

        seconds, message = parsed

        self.reminder_service.set_reminder(
            seconds,
            message
        )

        return f"Okay, I will remind you to {message}."

    def parse_reminder(self, command: str):
        pattern = (
            r"(?:remind me|set a reminder) in "
            r"(\d+) "
            r"(second|seconds|minute|minutes|hour|hours) "
            r"to (.+)"
        )

        match = re.search(
            pattern,
            command.lower()
        )

        if not match:
            return None

        amount = int(match.group(1))
        unit = match.group(2)
        message = match.group(3).strip()

        seconds = self.convert_to_seconds(
            amount,
            unit
        )

        return seconds, message

    def convert_to_seconds(
        self,
        amount: int,
        unit: str
    ) -> int:

        if unit.startswith("second"):
            return amount

        if unit.startswith("minute"):
            return amount * 60

        if unit.startswith("hour"):
            return amount * 3600

        raise ValueError("Unsupported time unit")
