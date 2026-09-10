#!/usr/bin/env python3
"""Module defining abstract class Shape, subclasses, and duck typing info."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a new Circle.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int, float): The width of the rectangle.
            height (int, float): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.

    Args:
        shape (object): Object expected to have area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
