import ast
import operator
import re

from commands.base_commands import BaseCommand
from config.logger import setup_logger


class CalculatorCommand(BaseCommand):

    def __init__(self):
        self.logger = setup_logger("CalculatorCommand")

        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }

    def execute(self, command: str) -> str:
        expression = self.extract_expression(command)

        if not expression:
            return "Please tell me what you want me to calculate."

        try:
            result = self.safe_calculate(expression)
            return f"The answer is {result}."

        except ZeroDivisionError:
            return "Division by zero is not allowed."

        except Exception as error:
            self.logger.exception(
                "Calculation failed: %s",
                error
            )

            return "Sorry, I could not calculate that expression."

    def extract_expression(self, command: str) -> str:
        expression = command.lower()

        replacements = {
            "calculate": "",
            "what is": "",
            "what's": "",
            "multiplied by": "*",
            "multiply by": "*",
            "times": "*",
            "divided by": "/",
            "divide by": "/",
            "plus": "+",
            "minus": "-",
            "to the power of": "**",
            "power": "**",
        }

        for phrase, replacement in replacements.items():
            expression = expression.replace(
                phrase,
                replacement
            )

        expression = re.sub(
            r"(?<=\d)\s*x\s*(?=\d)",
            " * ",
            expression
        )

        return expression.strip()

    def safe_calculate(self, expression: str):
        tree = ast.parse(
            expression,
            mode="eval"
        )

        return self._evaluate_node(tree.body)

    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value

            raise ValueError("Unsupported value")

        if isinstance(node, ast.BinOp):
            operator_type = type(node.op)

            if operator_type not in self.operators:
                raise ValueError(
                    "Unsupported operator"
                )

            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)

            return self.operators[
                operator_type
            ](left, right)

        if isinstance(node, ast.UnaryOp):
            operator_type = type(node.op)

            if operator_type not in self.operators:
                raise ValueError(
                    "Unsupported operator"
                )

            value = self._evaluate_node(
                node.operand
            )

            return self.operators[
                operator_type
            ](value)

        raise ValueError(
            "Unsupported expression"
        )