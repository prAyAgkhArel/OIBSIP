import unittest

from password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()

    def test_password_length(self):
        password = self.generator.generate_password(
            length=12,
            use_uppercase=True,
            use_lowercase=True,
            use_numbers=True,
            use_symbols=True
        )

        self.assertEqual(len(password), 12)

    def test_minimum_length_validation(self):
        with self.assertRaises(ValueError):
            self.generator.generate_password(
                length=5,
                use_uppercase=True,
                use_lowercase=True
            )

    def test_requires_two_character_types(self):
        with self.assertRaises(ValueError):
            self.generator.generate_password(
                length=12,
                use_uppercase=True,
                use_lowercase=False,
                use_numbers=False,
                use_symbols=False
            )

    def test_contains_selected_character_types(self):
        password = self.generator.generate_password(
            length=12,
            use_uppercase=True,
            use_lowercase=True,
            use_numbers=True,
            use_symbols=True
        )

        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(not char.isalnum() for char in password))

    def test_excludes_ambiguous_characters(self):
        password = self.generator.generate_password(
            length=30,
            use_uppercase=True,
            use_lowercase=True,
            use_numbers=True,
            use_symbols=False,
            exclude_ambiguous=True
        )

        ambiguous = "0O1lI"

        for char in ambiguous:
            self.assertNotIn(char, password)


if __name__ == "__main__":
    unittest.main()