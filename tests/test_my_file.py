"""Tests for the my_file module."""

import unittest
from sample_package.my_file import generate_random_password


class TestMyFile(unittest.TestCase):
    """Test cases for the my_file module."""

    def test_generate_random_password(self):
        """Test that generate_random_password returns a 12-character string."""
        print("Testing generate_random_password")
        self.assertEqual(len(generate_random_password()), 12)

    def test_generate_random_password_length(self):
        """Test that generate_random_password returns a password of
        specified length."""
        print("Testing generate_random_password_length")
        password = generate_random_password(length=16)
        self.assertEqual(len(password), 16)


if __name__ == '__main__':
    unittest.main()
