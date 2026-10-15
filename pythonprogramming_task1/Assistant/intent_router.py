import re


class IntentRouter:

    def get_intent(self, command: str) -> str:
        command = command.lower().strip()

        if self._is_exit(command):
            return "exit"
        
        if self._is_email(command):
            return "email"

        if self._is_greeting(command):
            return "greeting"

        if self._is_calculator(command):
            return "calculator"

        if self._is_time(command):
            return "time"

        if self._is_date(command):
            return "date"
        
        if self._is_knowledge(command):
           return "knowledge"

        if self._is_search(command):
            return "search"

        if self._is_weather(command):
            return "weather"

        if self._is_reminder(command):
            return "reminder"

        return "unknown"

    def _is_exit(self, command: str) -> bool:
        exit_phrases = [
            "exit",
            "quit",
            "stop",
            "goodbye",
            "bye"
        ]

        return command in exit_phrases




    def _is_greeting(self, command: str) -> bool:
        greeting_words = [
            "hello",
            "hi",
            "hey"
        ]

        for word in greeting_words:
            if re.search(rf"\b{re.escape(word)}\b", command):
                return True

        return False

    def _is_calculator(self, command: str) -> bool:
        math_words = [
            "calculate",
            "plus",
            "minus",
            "times",
            "multiplied by",
            "multiply by",
            "divided by",
            "divide by",
            "power"
        ]

        if any(word in command for word in math_words):
            return True

        if re.search(r"\d+\s*[\+\-\*/]\s*\d+", command):
            return True

        return False

    def _is_time(self, command: str) -> bool:
        return "time" in command

    def _is_date(self, command: str) -> bool:
        return "date" in command

    def _is_search(self, command: str) -> bool:
        search_phrases = [
            "search",
            "search for",
            "look up",
            "find information about",
            "about"
        ]

        return any(
            phrase in command
            for phrase in search_phrases
        )

    def _is_weather(self, command: str) -> bool:
        weather_phrases = [
            "weather",
            "temperature",
            "forecast"
        ]

        return any(
            phrase in command
            for phrase in weather_phrases
        )

    def _is_reminder(self, command: str) -> bool:
        reminder_phrases = [
            "remind me",
            "set a reminder",
            "reminder"
        ]

        return any(
            phrase in command
            for phrase in reminder_phrases
        )

    def _is_email(self, command: str) -> bool:
        email_phrases = [
            "send email",
            "send an email",
            "email"
        ]

        return any(
            phrase in command
            for phrase in email_phrases
        )
    
    def _is_knowledge(self, command: str) -> bool:
        knowledge_starters = [
            "what is",
            "who is",
            "where is",
            "when is",
            "why is",
            "how does",
            "tell me about"
        ]

        return any(
            command.startswith(phrase)
            for phrase in knowledge_starters
        )