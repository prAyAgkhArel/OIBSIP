# This is a BMI calculator

import tkinter as tk

from gui import BMIApp


def main():
    window = tk.Tk()
    BMIApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()