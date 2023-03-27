#!usr/bin/python3

class List(list):
    """
    The `List` class is a subclass of the built-in `list` class
    in Python. It adds a single method `print` to the `list` class.
    """
    def print(self) -> None:

        print(*self, sep="\n")
