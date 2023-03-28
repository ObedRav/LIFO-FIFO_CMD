#!/usr/bin/python3
"""
This code is responsible for initializing and configuring a data
structure and a persistence mechanism based on environmental variables.
"""
from os import getenv
from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage


def get_storage():
    storage_type = getenv('STORAGE', 'file')
    if storage_type == 'database':
        return DBStorage()
    else:
        return FileStorage()

storage = get_storage()

print(f"You're using {storage.__class__.__name__} as a persistence")
