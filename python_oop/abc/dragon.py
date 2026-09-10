#!/usr/bin/env python3
"""Module demonstrating modular functionality using Mixins."""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print swimming functionality."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print flying functionality."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon combining swimming and flying capabilities."""

    def roar(self):
        """Print dragon roaring behavior."""
        print("The dragon roars!")
