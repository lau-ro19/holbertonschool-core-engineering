#!/usr/bin/env python3
"""Module that provides a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return character count.

    Args:
        filename (str): The path to the file to write to.
        text (str): The string content to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
