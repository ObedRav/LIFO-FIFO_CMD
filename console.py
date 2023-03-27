#!usr/bin/python3

import cmd
import os
from classes.doubly_linked_list import LinkedList
from classes.list import List

data_structure = os.getenv('DATA_STRUCTURE')

if data_structure.lower() == 'linkedlist':
    data_structure = LinkedList
else:
    data_structure = List


class LIFO_FIFO_CONSOLE(cmd.Cmd):
    prompt = "> "

