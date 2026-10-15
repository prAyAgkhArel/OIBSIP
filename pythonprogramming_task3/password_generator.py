import secrets
import string


class PasswordGenerator:
    def __init__(self):
        self.ambiguous_characters = "0O1lI"

    def generate_password(
        self,
        length,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
        exclude_ambiguous=False
    ):
        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        selected_sets = []

        if use_uppercase:
            selected_sets.append(string.ascii_uppercase)

        if use_lowercase:
            selected_sets.append(string.ascii_lowercase)

        if use_numbers:
            selected_sets.append(string.digits)

        if use_symbols:
            selected_sets.append(string.punctuation)

        if len(selected_sets) < 2:
            raise ValueError("Select at least two character types.")

        if exclude_ambiguous:
            cleaned_sets = []

            for character_set in selected_sets:
                cleaned_set = "".join(
                    character
                    for character in character_set
                    if character not in self.ambiguous_characters
                )

                cleaned_sets.append(cleaned_set)

            selected_sets = cleaned_sets

        password_characters = []

        # Guarantee at least one character from each selected type
        for character_set in selected_sets:
            password_characters.append(
                secrets.choice(character_set)
            )

        all_characters = "".join(selected_sets)

        remaining_length = length - len(password_characters)

        for _ in range(remaining_length):
            password_characters.append(
                secrets.choice(all_characters)
            )

        # Shuffle securely
        secrets.SystemRandom().shuffle(password_characters)

        return "".join(password_characters)
    
    
