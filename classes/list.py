#!usr/bin/python3
"""
Module Name: 
list

Module Description:
This module contains one class which is a subclass of the built-in `list`

Module Classes:
- List(list)

Module Attributes:
- None
"""

class List(list):
    """
    The `List` class is a subclass of the built-in `list` class in Python.
    It adds several methods to the `list` class, including `print`, `pint`,
    `add`, `swap`, `to_dict`, `save`, and `reload`.
    """
    def print(self) -> None:
        """
        Prints the elements in the list separated by a newline character.
        """
        if self:
            print(*self, sep="\n")

    def pint(self) -> None:
        """
        Prints the first element in the list.
        """
        print(self[0])

    def add(self, value) -> None:
        """
        Adds a value to the second position in the list.
        """
        self.insert(1, value)

    def swap(self) -> None:
        """
        Swaps the first two elements in the list.
        """
        self[0], self[1] = self[1], self[0]

    def to_dict(self) -> dict:
        """
        Converts the list to a dictionary with a single key "data".
        """
        return {"data": self}

    def save(self) -> None:
        """
        Saves the list depending on the `storage` module.
        """
        from .__init__ import storage

        dict_list = self.to_dict()
        storage.save(dict_list)

    def reload(self):
        """
        Loads the list depending on the `storage`
        module and appends the elements to the list.
        """
        from .__init__ import storage
        data = storage.reload()

        if data is not None:
            for value in list(data.values())[0]:
                self.append(value)
