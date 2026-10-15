import unittest

from commands.calculator import CalculatorCommand


class TestCalculatorCommand(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorCommand()

    def test_addition(self):
        result = self.calculator.execute(
            "calculate 5 plus 7"
        )

        self.assertEqual(
            result,
            "The answer is 12."
        )

    def test_multiplication(self):
        result = self.calculator.execute(
            "calculate 6 times 4"
        )

        self.assertEqual(
            result,
            "The answer is 24."
        )

    def test_division(self):
        result = self.calculator.execute(
            "calculate 20 divided by 4"
        )

        self.assertEqual(
            result,
            "The answer is 5.0."
        )

    def test_division_by_zero(self):
        result = self.calculator.execute(
            "calculate 5 divided by 0"
        )

        self.assertEqual(
            result,
            "Division by zero is not allowed."
        )


if __name__ == "__main__":
    unittest.main()
