#!/usr/bin/env python3
"""Module that defines a Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
