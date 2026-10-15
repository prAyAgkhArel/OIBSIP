# Voice Assistant Project

A Python-based voice assistant built using Object-Oriented Programming principles.  
The assistant can recognize voice commands, speak responses, perform calculations, search the web, check weather, set reminders, send emails, answer basic knowledge questions, and execute custom commands.

## Features

- Voice input using SpeechRecognition
- Text-to-speech using pyttsx3
- Greeting responses
- Date and time information
- Web search
- Calculator
- Weather information using OpenWeather API
- Timed reminders
- Email sending using SMTP
- Confirmation before sending emails
- General knowledge lookup
- Custom commands
- Logging and error handling
- Unit testing

## Environment Variables
Create a .env file in the project root.
ASSISTANT_NAME=Nova
USER_NAME=User

WEATHER_API_KEY=your_openweather_api_key

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

SMTP_HOST=smtp.gmail.com
SMTP_PORT=465

# Example Commands

hello
what time is it
what is the date
calculate 5 plus 7
calculate 6 times 4
search for Python tutorials
weather in Kathmandu
remind me in 10 seconds to drink water
what is Python
open youtube
send email to example at gmail dot com subject hello message this is a test
goodbye

# Weather
Weather information is retrieved using the OpenWeather API.
Example:
weather in Kathmandu
The assistant returns information such as:
- Temperature
- Feels-like temperature
- Weather condition
- Humidity

![Asked Weather in Pokhara](<Screenshot 2026-10-15 104106.png>)


# Calculator
The calculator supports operations such as:
- Addition
- Subtraction
- Multiplication
- Division
- Powers
- Modulus
The calculator uses Python's ast module instead of directly using eval().
Example:
calculate 5 plus 7
calculate 6 times 4
calculate 20 divided by 5

![Response to some calculations](<Screenshot 2026-10-15 104525.png>)


# Reminders
The assistant can create timed reminders using background threads.
Example:
remind me in 30 seconds to drink water
The assistant continues listening while the reminder runs in the background.


# Email
Email is sent using Python's smtplib.
Example:
send email to example at gmail dot com subject hello message this is a test
Before sending, the assistant asks for confirmation.
Should I send it?
The user can respond with:
yes
or:
no
For Gmail, use a Google App Password instead of the normal Gmail password.

![Email Sending by SMTP](<Screenshot 2026-10-14 194816.png>)
![Email Sent Succesfully](<Screenshot 2026-10-14 194846.png>)
![Delivery of Email](<Screenshot 2026-10-14 194913.png>)

# Custom Commands
Custom commands are stored inside:
data/custom_commands.json
Example:
{
    "open youtube": {
        "action": "open_url",
        "value": "https://www.youtube.com",
        "response": "Opening YouTube."
    }
}
This allows new commands to be added without modifying the main Python code.

# General Knowledge
Basic knowledge questions are stored in:
data/knowledge_base.json
Example:
what is Python
The assistant searches the local knowledge base and returns the stored answer.
![Response to a general question](<Screenshot 2026-10-14 195752.png>)

# Logging
Application events and errors are recorded in:
logs/assistant.log
Logging helps with debugging and tracking application behavior.
Sensitive information such as passwords should never be written to the log file.

# Testing
Run all unit tests using:
>>python -m unittest discover -s tests -p "test_*.py"
The tests check features such as:
- Intent routing
- Calculator operations
- Knowledge lookup
- Email parsing
- Reminder time conversion
![Tests Result](<Screenshot 2026-10-15 104654.png>)


## Project Structure

```text
Voice_assistant/
│
├── main.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── Assistant/
│   ├── __init__.py
│   ├── voice_assistant.py
│   ├── speech_recognizer.py
│   ├── speaker.py
│   └── intent_router.py
│
├── commands/
│   ├── __init__.py
│   ├── base_command.py
│   ├── greeting.py
│   ├── datetime_command.py
│   ├── web_search.py
│   ├── calculator.py
│   ├── weather.py
│   ├── reminder.py
│   ├── email_command.py
│   ├── knowledge.py
│   └── custom_commands.py
│
├── Services/
│   ├── __init__.py
│   ├── weather_service.py
│   ├── reminder_service.py
│   ├── email_service.py
│   ├── knowledge_service.py
│   └── custom_command_service.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logger.py
│
├── data/
│   ├── knowledge_base.json
│   └── custom_commands.json
│
├── logs/
│   └── assistant.log
│
└── tests/
    ├── __init__.py
    ├── test_intent_router.py
    ├── test_calculator.py
    ├── test_knowledge_service.py
    ├── test_email_command.py
    └── test_reminder.py  ```
```




#
