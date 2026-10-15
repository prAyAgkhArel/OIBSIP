from Assistant.voice_assistant import VoiceAssistant
from config.logger import setup_logger


logger = setup_logger("Main")


def main():
    assistant = VoiceAssistant()

    try:
        assistant.start()

    except KeyboardInterrupt:
        logger.info(
            "Assistant stopped by user"
        )

        print("\nAssistant stopped.")

    except Exception as error:
        logger.exception(
            "Fatal application error: %s",
            error
        )


if __name__ == "__main__":
    main()