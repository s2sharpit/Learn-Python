"""
Released by Guido Van Rossum in 1991

- Interpreted
- Dynamically Typed
- High level language
"""

apple: str = "apple"


# 109: Docstrings
def get_length(item: str) -> int:
    """
    Returns the total length of a string (excl. spaces)

    :params str item: The item that you want to get the length for.
    :return int: The length of the item as an int.
    :raises TypeError: If the item is not a string.
    """

    if isinstance(item, str):
        processed: str = ''.join(item.split())
        return len(processed)
    else:
        raise TypeError("The item must be a string")
