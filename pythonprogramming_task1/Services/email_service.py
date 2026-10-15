import smtplib
from email.message import EmailMessage
from config.logger import setup_logger


class EmailService:

    def __init__(
        self,
        sender_email: str,
        password: str,
        smtp_host: str,
        smtp_port: int
    ):
        self.sender_email = sender_email
        self.password = password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.logger = setup_logger("EmailService")

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str
    ):
        self.logger.info(
                    "Sending email to %s",
                    recipient
                )
        if not self.sender_email or not self.password:
            raise ValueError(
                "Email credentials are missing."
            )

        message = EmailMessage()

        message["From"] = self.sender_email
        message["To"] = recipient
        message["Subject"] = subject

        message.set_content(body)

        with smtplib.SMTP_SSL(
            self.smtp_host,
            self.smtp_port
        ) as server:

            server.login(
                self.sender_email,
                self.password
            )

            server.send_message(message)
            
        self.logger.info(
            "Email sent successfully to %s",
            recipient
        )
