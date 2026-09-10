#!/usr/bin/env python3
"""Module defining VerboseList extending the built-in list class."""


class VerboseList(list):
    """Custom list class providing notifications for modifications."""

    def append(self, item):
        """Append item to list and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list by appending elements from iterable and notify."""
        items_count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """Remove first occurrence of item and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item at given index (default last) and print notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
