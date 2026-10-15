import re


class EmailCommand:

    def __init__(self, email_service):
        self.email_service = email_service
        self.pending_email = None

    def prepare_email(self, command: str) -> str:
        email_data = self.parse_email(command)

        if email_data is None:
            return (
                "Please say the email in this format: "
                "send email to example at gmail dot com, "
                "subject hello, message this is a test."
            )

        recipient, subject, body = email_data

        self.pending_email = {
            "recipient": recipient,
            "subject": subject,
            "body": body
        }

        return (
            f"I am ready to send the email to {recipient} "
            f"with the subject {subject}. "
            "Should I send it?"
        )

    def confirm_send(self) -> str:
        if self.pending_email is None:
            return "There is no email waiting to be sent."

        email = self.pending_email

        try:
            self.email_service.send_email(
                email["recipient"],
                email["subject"],
                email["body"]
            )

            self.pending_email = None

            return "Email sent successfully."

        except Exception as error:
            print(f"Email error: {error}")

            return (
                "Sorry, I could not send the email."
            )

    def cancel(self) -> str:
        self.pending_email = None

        return "Email cancelled."

    def has_pending_email(self) -> bool:
        return self.pending_email is not None

    def parse_email(self, command: str):
        command = command.lower().strip()

        pattern = (
            r"send (?:an )?email to (.+?) "
            r"subject (.+?) "
            r"message (.+)"
        )

        match = re.search(pattern, command)

        if not match:
            return None

        recipient = match.group(1).strip()
        subject = match.group(2).strip()
        body = match.group(3).strip()

        recipient = self.normalize_email(
            recipient
        )

        if not self.is_valid_email(recipient):
            return None

        return recipient, subject, body

    def normalize_email(self, email: str) -> str:
        email = email.replace(" at ", "@")
        email = email.replace(" dot ", ".")
        email = email.replace(" ", "")

        return email

    def is_valid_email(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        return bool(
            re.match(pattern, email)
        )
