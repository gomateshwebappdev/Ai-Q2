"""
AI-Powered Code Generation and Debugging Assistant
Test Cases Module

This file contains unit tests for the string reversal and palindrome checker
using Python's built-in unittest module.

Test Command:
    python -m unittest -v test_cases.py

Expected Output Format:
    test_running_suite ... ok
    ...
   ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import main module functions
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import reverse_string, is_palindrome


class TestStringReversalAndPalindrome(unittest.TestCase):
    """Test cases for the string reversal and palindrome checker."""

    def test_palindrome_madam(self):
        """Test that 'madam' is recognized as a palindrome."""
        self.assertTrue(is_palindrome("madam"))

    def test_palindrome_hello(self):
        """Test that 'hello' is NOT a palindrome."""
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_level(self):
        """Test that 'level' is recognized as a palindrome."""
        self.assertTrue(is_palindrome("level"))

    def test_uppercase_input(self):
        """Test that uppercase input is handled case-insensitively."""
        self.assertTrue(is_palindrome("MADAM"))
        self.assertTrue(is_palindrome("Level"))

    def test_empty_input(self):
        """Test that empty input returns False."""
        self.assertFalse(is_palindrome(""))

    def test_single_character(self):
        """Test that a single character is considered a palindrome."""
        self.assertTrue(is_palindrome("a"))

    def test_reversal_madam(self):
        """Test that reversing 'madam' returns 'madam'."""
        self.assertEqual(reverse_string("madam"), "madam")

    def test_reversal_hello(self):
        """Test that reversing 'hello' returns 'olleh'."""
        self.assertEqual(reverse_string("hello"), "olleh")


if __name__ == "__main__":
    unittest.main()