from config.logger import setup_logger

from Assistant.speaker import Speaker
from Assistant.speech_recognizer import SpeechRecognizer
from Assistant.intent_router import IntentRouter

from commands.greetings import GreetingCommand
from commands.datetime_command import DateTimeCommand
from commands.websearch import WebSearchCommand
from commands.calculator import CalculatorCommand
from commands.weather import WeatherCommand
from Services.weather_service import WeatherService
from commands.reminder import ReminderCommand
from Services.reminder_service import ReminderService
from commands.email_command import EmailCommand
from Services.email_service import EmailService
from commands.knowledge import KnowledgeCommand
from Services.knowledge_service import KnowledgeService
from commands.custom_command import CustomCommand
from Services.custom_command_service import CustomCommandService

from config.settings import Settings


class VoiceAssistant:

    def __init__(self):
        self.settings = Settings()
        self.logger = setup_logger("VoiceAssistant")

        self.speaker = Speaker()
        self.recognizer = SpeechRecognizer()
        self.router = IntentRouter()

        self.greeting_command = GreetingCommand()
        self.datetime_command = DateTimeCommand()
        self.web_search_command = WebSearchCommand()
        self.calculator_command = CalculatorCommand()
        self.weather_service = WeatherService(
            self.settings.weather_api_key
        )
        self.weather_command = WeatherCommand(
            self.weather_service
        )
        self.reminder_service = ReminderService(
            self.speaker
        )
        self.reminder_command = ReminderCommand(
            self.reminder_service
        )
        self.email_service = EmailService(
            sender_email=self.settings.email_address,
            password=self.settings.email_password,
            smtp_host=self.settings.smtp_host,
            smtp_port=self.settings.smtp_port
        )

        self.email_command = EmailCommand(
            self.email_service
        )

        self.knowledge_service = KnowledgeService(
            "data/knowledge_base.json"
        )

        self.knowledge_command = KnowledgeCommand(
            self.knowledge_service
        )        
        self.custom_command_service = CustomCommandService(
            "data/custom_commands.json"
        )

        self.custom_command = CustomCommand(
            self.custom_command_service
        )

        self.running = True

    def start(self):

        self.logger.info("Assistant started")

        welcome_message = (
            f"{self.settings.assistant_name} is ready."
        )

        self.speaker.speak(welcome_message)

        while self.running:

            try:
                command = self.recognizer.listen()

                if not command:
                    continue

                self.logger.info(
                    "User command: %s",
                    command
                )

                self.handle_command(command)

            except Exception as error:
                self.logger.exception(
                    "Unexpected error in main loop: %s",
                    error
                )

                self.speaker.speak(
                    "Sorry, something went wrong."
                )

    def handle_command(self, command: str):

        if self.email_command.has_pending_email():

            if command in [
                "yes",
                "yes send it",
                "send it",
                "confirm"
            ]:
                response = self.email_command.confirm_send()
                self.speaker.speak(response)
                return

            if command in [
                "no",
                "cancel",
                "don't send it",
                "do not send it"
            ]:
                response = self.email_command.cancel()
                self.speaker.speak(response)
                return

            response = (
                "Please say yes to send the email "
                "or no to cancel it."
            )

            self.speaker.speak(response)
            return
        
        custom_response = self.custom_command.execute(command)

        if custom_response:
            self.speaker.speak(custom_response)
            return

        intent = self.router.get_intent(command)

        if intent == "greeting":
            response = self.greeting_command.execute(
                self.settings.user_name
            )

        elif intent == "time":
            response = self.datetime_command.get_time()

        elif intent == "date":
            response = self.datetime_command.get_date()

        elif intent == "search":
            response = self.web_search_command.execute(
                command
            )

        elif intent == "calculator":
            response = self.calculator_command.execute(
                command
            )

        elif intent == "weather":
            response = self.weather_command.execute(
                command
            )

        elif intent == "reminder":
            response = self.reminder_command.execute(
                command
            )

        elif intent == "email":
            response = self.email_command.prepare_email(
                command
            )
        
        elif intent == "knowledge":
            response = self.knowledge_command.execute(command)

        elif intent == "exit":
            response = "Goodbye! Have a great day."
            self.running = False
        

        else:
            response = (
                "Sorry, I don't understand that command yet."
            )

        self.speaker.speak(response)