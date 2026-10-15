from datetime import datetime


class DateTimeCommand:

    def get_time(self) -> str:
        now = datetime.now()

        return now.strftime(
            "The current time is %I:%M %p."
        )

    def get_date(self) -> str:
        now = datetime.now()

        return now.strftime(
            "Today is %A, %B %d, %Y."
        )