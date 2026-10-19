"""
AI-Powered Code Generation and Debugging Assistant
String Reversal and Palindrome Checker

This program demonstrates how Generative AI can help generate code,
explain program logic, identify programming errors, and debug faulty code.

Features:
- Accepts a string from the user
- Reverses and displays the string
- Checks whether the input is a palindrome (case-insensitive)
- Handles empty input and ordinary strings gracefully
- Uses functions for modular, readable code
"""

import unittest


def reverse_string(input_str):
    """
    Reverse the given string using Python slicing.

    Args:
        input_str (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    # Python slicing with [::-1] creates a reversed copy of the string
    reversed_str = input_str[::-1]
    return reversed_str


def is_palindrome(input_str):
    """
    Check if the given string is a palindrome (case-insensitive).

    A palindrome is a word, phrase, or sequence that reads the same
    forward and backward, ignoring spaces, punctuation, and capitalization.

    Args:
        input_str (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Handle empty string case
    if not input_str:
        return False

    # Convert to lowercase for case-insensitive comparison
    # Then compare the lowercase string with its reverse
    lowered = input_str.lower()
    reversed_lowered = lowered[::-1]

    # Check if the lowered string equals its reverse
    is_pal = lowered == reversed_lowered
    return is_pal


def main():
    """
    Main function to run the string reversal and palindrome checker.
    Accepts user input, displays results in a beginner-friendly format.
    """
    print("=" * 60)
    print("STRING REVERSAL AND PALINDROME CHECKER")
    print("=" * 60)

    # Accept input from the user
    user_input = input("\nEnter a string: ")

    # Display the original string
    print(f"\nOriginal string: '{user_input}'")

    # Reverse and display the string
    if user_input:
        reversed_str = reverse_string(user_input)
        print(f"Reversed string: '{reversed_str}'")
    else:
        print("No input provided for reversal.")

    # Check if the input is a palindrome
    if user_input:
        palindrome_result = is_palindrome(user_input)
        if palindrome_result:
            print(f"'{user_input}' IS a palindrome!")
        else:
            print(f"'{user_input}' is NOT a palindrome.")
    else:
        print("Cannot check palindrome for empty input.")

    print("\n" + "=" * 60)
    print("Program completed. Thank you for using the assistant!")
    print("=" * 60)


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()


###############################################################################
# UNIT TESTS
###############################################################################


class TestStringReversalAndPalindrome(unittest.TestCase):
    """Test cases for the string reversal and palindrome checker functions."""

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