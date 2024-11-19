"""Utility functions for password generation and management."""

import random
import string


def generate_random_password(length: int = 12) -> str:
    """Generate a random password with specified length.

    Args:
        length (int, optional): Length of password to generate. Defaults to 12.

    Returns:
        str: Random password containing letters, numbers and special characters

    Raises:
        ValueError: If length is less than 8
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"

    # Ensure at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill remaining length with random characters
    all_chars = lowercase + uppercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(length - 4))

    # Shuffle the password
    random.shuffle(password)
    return "".join(password)
