import unittest

from Assistant.intent_router import IntentRouter


class TestIntentRouter(unittest.TestCase):

    def setUp(self):
        self.router = IntentRouter()

    def test_greeting(self):
        self.assertEqual(
            self.router.get_intent("hello"),
            "greeting"
        )

    def test_calculator(self):
        self.assertEqual(
            self.router.get_intent("calculate 5 plus 4"),
            "calculator"
        )

    def test_weather(self):
        self.assertEqual(
            self.router.get_intent("weather in kathmandu"),
            "weather"
        )

    def test_email(self):
        self.assertEqual(
            self.router.get_intent(
                "send email to test at gmail dot com"
            ),
            "email"
        )

    def test_unknown(self):
        self.assertEqual(
            self.router.get_intent("abracadabra"),
            "unknown"
        )


if __name__ == "__main__":
    unittest.main()
