import requests


class WeatherCommand:

    def __init__(self, weather_service):
        self.weather_service = weather_service

    def execute(self, command: str) -> str:
        city = self.extract_city(command)

        if not city:
            return "Please tell me which city you want the weather for."

        try:
            weather = self.weather_service.get_weather(city)

            return (
                f"The weather in {weather['city']} is "
                f"{weather['description']}. "
                f"The temperature is {weather['temperature']:.1f} degrees Celsius, "
                f"and it feels like {weather['feels_like']:.1f} degrees. "
                f"Humidity is {weather['humidity']} percent."
            )

        except requests.exceptions.HTTPError:
            return (
                f"I could not find weather information for {city}."
            )

        except requests.exceptions.RequestException:
            return (
                "I could not connect to the weather service."
            )

        except Exception as error:
            print(f"Weather error: {error}")

            return (
                "Sorry, something went wrong while checking the weather."
            )

    def extract_city(self, command: str) -> str:
        command = command.lower()

        phrases = [
            "what is the weather in",
            "what's the weather in",
            "weather in",
            "temperature in",
            "forecast for"
        ]

        for phrase in phrases:
            if phrase in command:
                return command.replace(
                    phrase,
                    "",
                    1
                ).strip()

        return ""