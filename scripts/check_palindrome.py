#!/usr/bin/env python3
"""
check_palindrome.py

A simple script that checks whether a given word or phrase is a palindrome.
It ignores case, spaces, punctuation, and numeric characters.
"""

import re
import sys

def normalize(text: str) -> str:
    """Return a lowercase string containing only alphanumeric characters."""
    return re.sub(r'[^A-Za-z0-9]', '', text).lower()

def is_palindrome(text: str) -> bool:
    """Return True if the normalized text is a palindrome."""
    norm = normalize(text)
    return norm == norm[::-1]

def main() -> None:
    if len(sys.argv) > 1:
        # If arguments are provided, join them into a single string
        phrase = " ".join(sys.argv[1:])
    else:
        # Otherwise, prompt the user
        phrase = input("Enter a word or phrase to check: ")

    if is_palindrome(phrase):
        print(f'"{phrase}" is a palindrome.')
    else:
        print(f'"{phrase}" is not a palindrome.')

if __name__ == "__main__":
    main()
