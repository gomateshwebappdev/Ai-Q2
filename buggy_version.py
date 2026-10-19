"""
AI-Powered Code Generation and Debugging Assistant
BUGGY VERSION - String Reversal and Palindrome Checker

This file contains a deliberately introduced programming error suitable for
a beginner debugging exercise.

THE BUG: The is_palindrome function compares the original string directly
with its reverse without converting to lowercase first. This causes the
function to incorrectly report that uppercase strings (like "MADAM") are
NOT palindromes, even though they read the same forward and backward
when case is ignored.

Expected correct behavior: "MADAM" should be identified as a palindrome.
Buggy behavior: "MADAM" is identified as NOT a palindrome because
'A' != 'a' in direct comparison.
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
    reversed_str = input_str[::-1]
    return reversed_str


def is_palindrome(input_str):
    """
    BUGGY: Check if the given string is a palindrome.

    THE BUG: This function compares the original string directly with its
    reverse using case-sensitive comparison. It does NOT convert to lowercase
    before comparison, so uppercase letters are treated as different from
    their lowercase counterparts.

    Correct behavior should convert to lowercase first for case-insensitive
    comparison, as per the specification.

    Args:
        input_str (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
            NOTE: Due to the bug, this will incorrectly return False
            for uppercase palindromes like "MADAM".
    """
    # BUG: Direct comparison without case normalization
    # This causes "MADAM" != "madaM" even though they are palindromes
    reversed_str = input_str[::-1]

    # BUG SITE: This comparison is case-sensitive
    # Fix: Use input_str.lower() == input_str[::-1].lower()
    is_pal = (input_str == reversed_str)

    return is_pal


def main():
    """
    Main function for the buggy version.
    Demonstrates incorrect behavior with uppercase inputs.
    """
    print("=" * 60)
    print("BUGGY STRING REVERSAL AND PALINDROME CHECKER")
    print("=" * 60)

    user_input = input("\nEnter a string: ")

    print(f"\nOriginal string: '{user_input}'")

    if user_input:
        reversed_str = reverse_string(user_input)
        print(f"Reversed string: '{reversed_str}'")

        palindrome_result = is_palindrome(user_input)
        if palindrome_result:
            print(f"'{user_input}' IS a palindrome!")
        else:
            print(f"'{user_input}' is NOT a palindrome. (BUG: uppercase palindromes")
            print("  are incorrectly rejected due to case-sensitive comparison.)")

    print("\n" + "=" * 60)
    print("Program completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()


###############################################################################
# UNIT TESTS FOR BUGGY VERSION
###############################################################################


class TestBuggyStringReversalAndPalindrome(unittest.TestCase):
    """Test cases demonstrating the bug in the buggy version."""

    def test_uppercase_palindrome_bug(self):
        """
        This test demonstrates the bug: 'MADAM' should be a palindrome,
        but the buggy code incorrectly reports it as NOT a palindrome.
        """
        # The buggy is_palindrome will return False for "MADAM"
        # because of case-sensitive comparison
        result = is_palindrome("MADAM")
        # This test EXPECTS False due to the bug, but the correct answer
        # should be True (case-insensitive palindrome)
        self.assertFalse(result)

    def test_lowercase_palindrome(self):
        """Test that lowercase 'madam' passes even the buggy code."""
        result = is_palindrome("madam")
        self.assertTrue(result)

    def test_hello_not_palindrome(self):
        """Test that 'hello' is correctly identified as NOT a palindrome."""
        result = is_palindrome("hello")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()