import unittest

from commands.email_command import EmailCommand


class FakeEmailService:

    def send_email(
        self,
        recipient,
        subject,
        body
    ):
        pass


class TestEmailCommand(unittest.TestCase):

    def setUp(self):
        self.command = EmailCommand(
            FakeEmailService()
        )

    def test_email_parsing(self):
        result = self.command.parse_email(
            "send email to test at gmail dot com "
            "subject hello "
            "message this is a test"
        )

        self.assertIsNotNone(result)

        recipient, subject, body = result

        self.assertEqual(
            recipient,
            "test@gmail.com"
        )

        self.assertEqual(
            subject,
            "hello"
        )

        self.assertEqual(
            body,
            "this is a test"
        )


if __name__ == "__main__":
    unittest.main()
