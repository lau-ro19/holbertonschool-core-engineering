#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish inheriting from both Fish and Bird."""

    def fly(self):
        """Print soaring behavior of a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")
