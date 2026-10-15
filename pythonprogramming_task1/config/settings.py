import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()

        self.assistant_name = os.getenv(
            "ASSISTANT_NAME",
            "Nova"
        )

        self.user_name = os.getenv(
            "USER_NAME",
            "User"
        )

        self.weather_api_key = os.getenv(
            "WEATHER_API_KEY"
        )

        self.email_address = os.getenv(
            "EMAIL_ADDRESS"
        )

        self.email_password = os.getenv(
            "EMAIL_PASSWORD"
        )

        self.smtp_host = os.getenv(
            "SMTP_HOST",
            "smtp.gmail.com"
        )

        self.smtp_port = int(
            os.getenv("SMTP_PORT", "465")
        )