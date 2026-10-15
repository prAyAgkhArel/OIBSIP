import pyttsx3


class Speaker:
    def __init__(self):
        self.rate = 170
        self.volume = 1.0

    def speak(self, message: str):
        print(f"Assistant: {message}")

        try:
            engine = pyttsx3.init()

            engine.setProperty("rate", self.rate)
            engine.setProperty("volume", self.volume)

            engine.say(message)
            engine.runAndWait()

            engine.stop()

        except Exception as e:
            print(f"Text-to-speech error: {e}")