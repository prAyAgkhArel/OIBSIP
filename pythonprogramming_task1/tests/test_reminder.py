import unittest

from commands.reminder import ReminderCommand


class FakeReminderService:

    def set_reminder(
        self,
        seconds,
        message
    ):
        pass


class TestReminderCommand(unittest.TestCase):

    def setUp(self):
        self.command = ReminderCommand(
            FakeReminderService()
        )

    def test_seconds(self):
        result = self.command.convert_to_seconds(
            10,
            "seconds"
        )

        self.assertEqual(result, 10)

    def test_minutes(self):
        result = self.command.convert_to_seconds(
            5,
            "minutes"
        )

        self.assertEqual(result, 300)

    def test_hours(self):
        result = self.command.convert_to_seconds(
            2,
            "hours"
        )

        self.assertEqual(result, 7200)


if __name__ == "__main__":
    unittest.main()
