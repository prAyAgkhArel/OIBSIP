import speech_recognition as sr


class SpeechRecognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.8

    def listen(self) -> str:
        try:
            with sr.Microphone() as source:

                print("\nListening...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

            print("Recognizing...")

            command = self.recognizer.recognize_google(
                audio,
                language="en-US"
            )

            command = command.lower().strip()

            print(f"You: {command}")

            return command

        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""

        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""

        except sr.RequestError as error:
            print(
                f"Speech recognition service error: {error}"
            )
            return ""

        except OSError as error:
            print(f"Microphone error: {error}")
            return ""

        except Exception as error:
            print(f"Unexpected recognition error: {error}")
            return ""