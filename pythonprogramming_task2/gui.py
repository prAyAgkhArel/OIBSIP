import tkinter as tk
from tkinter import messagebox

from bmi_calculator import BMICalculator
from database import DatabaseManager

import matplotlib.pyplot as plt

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.calculator = BMICalculator()
        self.database = DatabaseManager()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="BMI Calculator",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=15)

        tk.Label(self.root, text="Name:").pack()
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack(pady=5)

        tk.Label(self.root, text="Weight (kg):").pack()
        self.weight_entry = tk.Entry(self.root, width=30)
        self.weight_entry.pack(pady=5)

        tk.Label(self.root, text="Height (m):").pack()
        self.height_entry = tk.Entry(self.root, width=30)
        self.height_entry.pack(pady=5)

        calculate_button = tk.Button(
            self.root,
            text="Calculate",
            command=self.calculate_bmi
        )
        calculate_button.pack(pady=15)
        
        history_button = tk.Button(
            self.root,
            text="View History",
            command=self.show_history
        )
        history_button.pack(pady=5)

        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold")
        )
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get().strip()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if not name:
                messagebox.showerror(
                    "Input Error",
                    "Please enter a name."
                )
                return

            if weight <= 0 or height <= 0:
                messagebox.showerror(
                    "Input Error",
                    "Weight and height must be positive values."
                )
                return

            bmi = self.calculator.calculate_bmi(weight, height)
            category = self.calculator.get_category(bmi)

            self.display_result(bmi, category)

            self.database.save_record(
                name,
                weight,
                height,
                bmi,
                category
            )

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid numbers for weight and height."
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )
    
    def show_history(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showerror(
                "Input Error",
                "Please enter a name to view history."
            )
            return

        try:
            history = self.database.get_user_history(name)

            if not history:
                messagebox.showinfo(
                    "History",
                    "No BMI history found for this user."
                )
                return

            dates = [record[0] for record in history]
            bmi_values = [record[1] for record in history]

            plt.figure()
            plt.plot(dates, bmi_values, marker="o")

            plt.title(f"BMI History - {name}")
            plt.xlabel("Date")
            plt.ylabel("BMI")

            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.show()

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def display_result(self, bmi, category):
        if category == "Normal":
            color = "green"
        elif category == "Underweight":
            color = "blue"
        elif category == "Overweight":
            color = "orange"
        else:
            color = "red"

        self.result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}",
            fg=color
        )