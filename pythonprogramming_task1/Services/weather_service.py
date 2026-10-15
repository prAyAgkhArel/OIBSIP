import requests
from config.logger import setup_logger


class WeatherService:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.logger = setup_logger("WeatherService")

    def get_weather(self, city: str) -> dict:
        
        self.logger.info(
            "Fetching weather for city: %s",
            city
        )
        if not self.api_key:
            raise ValueError("Weather API key is missing.")

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=5
        )

        response.raise_for_status()

        data = response.json()
        
        self.logger.info(
            "Weather data received successfully for city: %s",
            city
        )

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }