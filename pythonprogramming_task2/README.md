# BMI Calculator

A Python BMI calculator built using an object-oriented structure.

## Features

- Calculates Body Mass Index (BMI)
- Classifies BMI as:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Validates user input
- Provides color-coded BMI results
- Supports multiple users by name
- Stores BMI records using SQLite
- Displays BMI history using Matplotlib
- Uses a Tkinter graphical user interface
![Interface](<Screenshot 2026-10-15 105836.png>)


## Project Structure

```text
bmi_calculator/
├── main.py
├── bmi_calculator.py
├── database.py
├── gui.py
├── requirements.txt
└── bmi_records.db

```
# Installation

pip install -r requirements.txt

# Run the Program 
python main.py

# BMI formula

BMI = weight/height^2 
weight in kilograms
height in meters