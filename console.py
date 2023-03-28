#!/usr/bin/python3

import cmd
from os import getenv
from classes.doubly_linked_list import LinkedList
from classes.list import List

def get_data_structure():
    """
    Obtaining the data structure of a environment variable
    """
    data_structure_type = getenv('DATA_STRUCTURE', 'list')
    if data_structure_type.lower() == 'linkedlist':
        return LinkedList()
    else:
        return List()

data_structure = get_data_structure()
data_structure.reload()


class LIFO_FIFO_CONSOLE(cmd.Cmd):
    """
    This class is a command-line interface (CLI) that allows you to
    interact with a LIFO (Last-In, First-Out) or FIFO (First-In, First-Out)
    data structure, depending on the implementation used.
    """

    intro = f"You're using {data_structure.__class__.__name__} as a data_structure"
    prompt = f"({data_structure.__class__.__name__})> "

    def do_push(self, args):
        """
        This method adds an element to the top of the data structure.
        The argument 'args' is expected to contain the number to be added.
        If the argument is not an integer, an error message is displayed.
        """
        # desestructuring the args
        number, *_ = args

        # Checking if is an integer
        try:
            number = int(number)
        except Exception:
            print("Invalid data, must be an integer")
            return

        # Adding element
        data_structure.append(number)

    def do_pop(self, args):
        """
        This method removes an element from the top
        of the data structure and displays it.
        """
        try:
            print(data_structure.pop())
        except IndexError:
            print("There are no elements in the data structure")
            return

    def do_pall(self, args):
        """
        This method displays every member of the data structure.
        """
        data_structure.print()

    def do_quit(self, args):
        """
        This method saves the data structure and quits from the CLI.
        """
        data_structure.save()
        return True

    def do_pint(self, args):
        """
        This method displays the member value at the top of the data structure.
        """
        try:
            data_structure.pint()
        except IndexError:
            print("There are no elements in the data structure")
            return

    def do_add(self, args):
        """
        This method adds the top two member values of the data structure.
        If the argument is not an integer, an error message is displayed.
        """
        # desestructuring the args
        number, *_ = args

        # Checking if is integer
        try:
            number = int(number)
        except Exception:
            print("Invalid data, must be an integer")
            return

        # Adding as a second argument
        data_structure.add(number)

    def do_swap(self, args):
        """
        This method swaps the order of the first and second
        elements in the data structure.
        """
        data_structure.swap()


if __name__ == "__main__":
    LIFO_FIFO_CONSOLE().cmdloop()
