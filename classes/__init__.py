"""
This code is responsible for initializing and configuring a data
structure and a persistence mechanism based on environmental variables.
"""
import os
from .doubly_linked_list import LinkedList
from .list import List
from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage


def get_storage():
    storage_type = os.getenv('STORAGE', 'file')
    if storage_type == 'database':
        return DBStorage()
    else:
        return FileStorage()

def get_data_structure():
    data_structure_type = os.getenv('DATA_STRUCTURE', 'list')
    if data_structure_type.lower() == 'linkedlist':
        return LinkedList()
    else:
        return List()

storage = get_storage()
data_structure = get_data_structure()
data_structure.reload()

print(f"You're using {storage.__class__.__name__} as a persistence")
