import threading
from config.logger import setup_logger

class ReminderService:
    def __init__(self, speaker):
        self.speaker = speaker
        self.active_reminders = []
        self.logger = setup_logger("ReminderService")

    def set_reminder(self, seconds: int, message: str):
        timer = threading.Timer(
            seconds,
            self._trigger_reminder,
            args=[message]
        )
        
        self.logger.info(
            "Reminder scheduled in %s seconds",
            seconds
        )

        timer.daemon = True
        timer.start()

        self.active_reminders.append(timer)

    def _trigger_reminder(self, message: str):
        reminder_message = f"Reminder: {message}"

        print(reminder_message)
        self.logger.info(
            "Reminder triggered"
        )

        self.speaker.speak(reminder_message)
