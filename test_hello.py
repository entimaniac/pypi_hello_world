"""Tests for the hello function."""

import unittest
from entimaniac_hello_world import hello


class TestHello(unittest.TestCase):
    """Test cases for the hello function."""

    def test_hello_with_simple_name(self):
        """Test hello function with a simple name."""
        result = hello("World")
        self.assertEqual(result, "Hello World")

    def test_hello_with_different_name(self):
        """Test hello function with a different name."""
        result = hello("Alice")
        self.assertEqual(result, "Hello Alice")

    def test_hello_with_empty_string(self):
        """Test hello function with an empty string."""
        result = hello("")
        self.assertEqual(result, "Hello ")

    def test_hello_with_special_characters(self):
        """Test hello function with special characters."""
        result = hello("John Doe")
        self.assertEqual(result, "Hello John Doe")

    def test_hello_with_none(self):
        """Test hello function with None value."""
        with self.assertRaises(TypeError):
            hello(None)


if __name__ == "__main__":
    unittest.main()

