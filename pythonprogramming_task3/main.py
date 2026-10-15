# This is a password generator project
import tkinter as tk
from tkinter import messagebox
import pyperclip

from password_generator import PasswordGenerator


class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.generator = PasswordGenerator()
        self.password_history = []

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Random Password Generator",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=15)

        # Password length
        tk.Label(
            self.root,
            text="Password Length:"
        ).pack()

        self.length_var = tk.IntVar(value=12)

        self.length_spinbox = tk.Spinbox(
            self.root,
            from_=8,
            to=50,
            textvariable=self.length_var,
            width=10
        )
        self.length_spinbox.pack(pady=5)

        # Character type variables
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.ambiguous_var = tk.BooleanVar(value=False)

        tk.Label(
            self.root,
            text="Character Types:",
            font=("Arial", 11, "bold")
        ).pack(pady=(15, 5))

        tk.Checkbutton(
            self.root,
            text="Uppercase Letters",
            variable=self.uppercase_var
        ).pack()

        tk.Checkbutton(
            self.root,
            text="Lowercase Letters",
            variable=self.lowercase_var
        ).pack()

        tk.Checkbutton(
            self.root,
            text="Numbers",
            variable=self.numbers_var
        ).pack()

        tk.Checkbutton(
            self.root,
            text="Symbols",
            variable=self.symbols_var
        ).pack()

        tk.Checkbutton(
            self.root,
            text="Exclude Ambiguous Characters",
            variable=self.ambiguous_var
        ).pack(pady=5)

        # Generate button
        generate_button = tk.Button(
            self.root,
            text="Generate Password",
            command=self.generate_password,
            width=20
        )
        generate_button.pack(pady=15)

        # Password display
        tk.Label(
            self.root,
            text="Generated Password:"
        ).pack()

        self.password_entry = tk.Entry(
            self.root,
            width=40,
            justify="center",
            font=("Arial", 12)
        )
        self.password_entry.pack(pady=5)

        # Strength indicator
        self.strength_label = tk.Label(
            self.root,
            text="Strength: -",
            font=("Arial", 11, "bold")
        )
        self.strength_label.pack(pady=5)

        # Copy button
        copy_button = tk.Button(
            self.root,
            text="Copy to Clipboard",
            command=self.copy_password,
            width=20
        )
        copy_button.pack(pady=10)

        # History
        tk.Label(
            self.root,
            text="Last 5 Passwords:",
            font=("Arial", 11, "bold")
        ).pack(pady=(15, 5))

        self.history_listbox = tk.Listbox(
            self.root,
            width=45,
            height=5
        )
        self.history_listbox.pack()

    def generate_password(self):
        try:
            length = self.length_var.get()

            password = self.generator.generate_password(
                length=length,
                use_uppercase=self.uppercase_var.get(),
                use_lowercase=self.lowercase_var.get(),
                use_numbers=self.numbers_var.get(),
                use_symbols=self.symbols_var.get(),
                exclude_ambiguous=self.ambiguous_var.get()
            )

            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)

            strength = self.check_strength(password)
            self.strength_label.config(
                text=f"Strength: {strength}"
            )

            self.update_history(password)

        except ValueError as error:
            messagebox.showerror(
                "Invalid Input",
                str(error)
            )

        except tk.TclError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid password length."
            )

    def check_strength(self, password):
        length = len(password)

        character_types = 0

        if any(char.isupper() for char in password):
            character_types += 1

        if any(char.islower() for char in password):
            character_types += 1

        if any(char.isdigit() for char in password):
            character_types += 1

        if any(not char.isalnum() for char in password):
            character_types += 1

        if length >= 16 and character_types >= 4:
            return "Strong"

        elif length >= 12 and character_types >= 3:
            return "Medium"

        else:
            return "Weak"

    def copy_password(self):
        password = self.password_entry.get()

        if password:
            pyperclip.copy(password)

            messagebox.showinfo(
                "Copied",
                "Password copied to clipboard."
            )

        else:
            messagebox.showwarning(
                "No Password",
                "Generate a password first."
            )

    def update_history(self, password):
        self.password_history.insert(0, password)

        self.password_history = self.password_history[:5]

        self.history_listbox.delete(0, tk.END)

        for saved_password in self.password_history:
            self.history_listbox.insert(
                tk.END,
                saved_password
            )


root = tk.Tk()
app = PasswordApp(root)
root.mainloop()
