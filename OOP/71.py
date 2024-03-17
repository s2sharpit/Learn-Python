"""
Protocols

Description:
Protocols define a set of methods and properties that a class must implement to satisfy the requirements of the protocol. They're useful for defining interfaces without using inheritance.

Usage:
- Protocols are used to specify expected behavior without enforcing inheritance.
- They allow different classes to fulfill a common interface even if they don't inherit from a common base class.
"""

from typing import Protocol


class Printable(Protocol):
    """Protocol: Defines methods and properties for printable items."""

    pages: int

    def print(self):
        """Method: Print the item."""
        pass

    def recycle(self):
        """Method: Recycle the item."""
        pass


class Book:
    """Class: Represents a book."""

    pages: int
    edition: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        """Method: Print the book."""
        print("Printing book:", self.title)

    def recycle(self):
        """Method: Recycle the book."""
        print("Recycling book:", self.title)

    def burn(self):
        """Method: Burn the book."""
        print("Burning book:", self.title)


class Magazine:
    """Class: Represents a magazine."""

    pages: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        """Method: Print the magazine."""
        print("Printing magazine:", self.title)

    def recycle(self):
        """Method: Recycle the magazine."""
        print("Recycling magazine:", self.title)


def print_item(printable: Printable):
    """Function: Print the given printable item."""
    printable.print()
    # printable.recycle()


book: Printable = Book("Python")
print_item(book)

magazine: Printable = Magazine("Deluxe Magazine")
print_item(magazine)
