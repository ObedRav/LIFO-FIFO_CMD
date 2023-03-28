import json
from os import path


class FileStorage:
    """
    The FileStorage class is used to save and load data from a JSON file.
    """

    def __init__(self, file_path="storage.json"):
        """
        The FileStorage class has a constructor that takes a file_path argument.
        If no argument is provided, it defaults to "storage.json". The file_path
        parameter is used to specify the location of the JSON file to be read from and written to.
        """
        self.file_path = file_path

    def save(self, data: dict) -> None:
        """
        The save method writes a Python dictionary to the JSON file specified by the
        file_path parameter. The data will be written in an indented JSON format.
        """
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def reload(self) -> dict:
        """
        The reload method reads a JSON file specified by the file_path parameter and
        returns its content as a Python dictionary. If the file does not exist, it returns None.
        """
        if path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return data
        else:
            return None
