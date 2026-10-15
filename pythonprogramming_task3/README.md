# Random Password Generator

A Python application that generates strong and secure random passwords based on user-selected criteria.

The application uses Python's `secrets` module for cryptographically secure password generation and provides a Tkinter-based graphical user interface.

## Features

- Generate random passwords with a minimum length of 8 characters
- Select character types:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Requires at least two character types
- Uses the `secrets` module for secure password generation
- Guarantees at least one character from every selected character type
- Password strength indicator:
  - Weak
  - Medium
  - Strong
- Option to exclude ambiguous characters such as:
  - `0`
  - `O`
  - `1`
  - `l`
  - `I`
- Copy generated passwords to the clipboard
- Displays the last 5 generated passwords during the current session
- Input validation for invalid password lengths and character selections
![Interface](<Screenshot 2026-10-15 110022.png>)

## Technologies Used

- Python
- Tkinter
- secrets
- string
- pyperclip
- unittest

## Project Structure

```text
Random_Password_Generator/
│
├── main.py
├── password_generator.py
├── requirements.txt
├── README.md
│
└── tests/
    ├── __init__.py
    └── test_password_generator.py
```

# Installing dependencies
pip install -r requirements.txt

# to run application
python main.py

# to run tests
python -m unittest discover
if all test passes, the output should show OK.

# Working Flow
The user selects a password length and chooses the character types to include.
The program creates character sets based on the selected options and uses secrets.choice() to select secure random characters.
At least one character from each selected category is added to the password before the remaining characters are generated.
The characters are then securely shuffled before the completed password is displayed.



