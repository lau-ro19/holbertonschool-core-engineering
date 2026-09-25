#!/usr/bin/env python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file and return added count.

    Args:
        filename (str): The path to the file to append to.
        text (str): The string content to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
