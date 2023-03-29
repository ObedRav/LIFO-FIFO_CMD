#!/usr/bin/python3
"""
Module Name: 
console

Module Description:
This module contains one function and one class which manage the console

Module Functions:
- get_data_structure() -> LinkedList | List

Module Classes:
- LIFO_FIFO_CONSOLE(cmd.Cmd)

Module Attributes:
- None
"""
import cmd
from os import getenv
from classes.doubly_linked_list import LinkedList
from classes.list import List 
from typing import Union
import sys


def get_data_structure() -> Union[LinkedList, List]:
    """
    Obtaining the data structure of a environment variable
    """
    data_structure_type = getenv('DATA_STRUCTURE', 'list')
    if data_structure_type.lower() == 'linkedlist':
        return LinkedList()
    else:
        return List()

# Obtaining the data structure and reloading the data
data_structure = get_data_structure()
data_structure.reload()


class LIFO_FIFO_CONSOLE(cmd.Cmd):
    """
    This class is a command-line interface (CLI) that allows you to
    interact with a LIFO (Last-In, First-Out) or FIFO (First-In, First-Out)
    data structure, depending on the implementation used.
    """

    if sys.__stdin__.isatty():
        intro = f"You're using {data_structure.__class__.__name__} as a data_structure"
        prompt = f"({data_structure.__class__.__name__})> "
    else:
        prompt = ""

    def do_push(self, args: str) -> None:
        """
        This method adds an element to the top of the data structure.
        The argument 'args' is expected to contain the number to be added.
        If the argument is not an integer, an error message is displayed.
        """   
        try:
            # destructuring the args and discarding the following fields
            number, *_ = args
            # Checking if can be parse to an integer
            number = int(number)
        except ValueError:
            print("Invalid data, must be an integer")
            return

        # Adding as a second argument
        data_structure.append(number)

    def do_add(self, args: str) -> None:
        """
        This method adds the top two member values of the data structure.
        If the argument is not an integer, an error message is displayed.
        """
        try:
            # destructuring the args and discarding the following fields
            number, *_ = args
            # Checking if can be parse to an integer
            number = int(number)
        except ValueError:
            print("Invalid data, must be an integer")
            return

        # Adding as a second argument
        data_structure.add(number)

    def do_swap(self, args: str) -> None:
        """
        This method swaps the order of the first and second
        elements in the data structure.
        """
        try:
            data_structure.swap()
        except IndexError:
            print("There are no enough elements in the data structure")
            return

    def do_pall(self, args: str) -> None:
        """
        This method displays every member of the data structure.
        """
        data_structure.print()

    def do_pint(self, args: str) -> None:
        """
        This method displays the member value at the top of the data structure.
        """
        try:
            data_structure.pint()
        except IndexError:
            print("There are no elements in the data structure")
            return

    def do_pop(self, args: str) -> None:
        """
        This method removes an element from the top
        of the data structure and displays it.
        """
        try:
            print(data_structure.pop())
        except IndexError:
            print("There are no elements in the data structure")
            return

    def do_quit(self, args: str) -> bool:
        """
        This method saves the data structure and quits from the CLI.
        """
        data_structure.save()
        return True

    def do_EOF(self, args: str) -> bool:
        """
        This method saves the data structure and quits from the CLI.
        """
        data_structure.save()
        return True

    def cmdloop(self, intro=None):
        try:
            return super().cmdloop(intro=intro)
        except KeyboardInterrupt:
            print("KeyboardInterrupt detected. Saving data and quitting...")
            data_structure.save()
            return True



if __name__ == "__main__":
    LIFO_FIFO_CONSOLE().cmdloop()
