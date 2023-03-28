#!usr/bin/python3
import sqlite3


class DBStorage:
    """
    The DBStorage class is used to save and load data from a database.
    """
    
    def create_table(self, conn: sqlite3.connect):
        """
        Creates a table in the database with the name "data" and a single column "number".

        Args:
        conn: Connection object that is used to connect to the database.
        """
        conn.execute('''CREATE TABLE IF NOT EXISTS data
                        (number INTEGER NOT NULL)''')

    def connect(self) -> sqlite3.connect:
        """
        Creates a connection to the SQLite database 'database.db'
        """
        return sqlite3.connect('database.db')

    def save(self, data_dict: dict) -> None:
        """
        Saves data from a dictionary to the "data" table in the database.

        Args:
        dict: A dictionary containing the data to be saved. The keys in the dictionary
              are ignored, and only the values are saved.
        """
        with self.connect() as conn:
            self.create_table(conn)
            values = list(data_dict.values())[0]
            for value in values:
                conn.execute(f"INSERT INTO data (number) VALUES ({value})")
            conn.commit()

    def reload(self) -> dict:
        """
        Retrieves data from the "data" table in the database, deletes
        the data from the table and returns the data in a dictionary.

        Returns:
        A dictionary containing the retrieved data. The keys in the dictionary
        are all "data", and the values are a list of integers that represent the
        data. If the "data" table is empty, an empty list is returned.
        """
        with self.connect() as conn:
            self.create_table(conn)
            cursor = conn.execute("SELECT number FROM data")
            result = [row[0] for row in cursor]
            conn.execute("DELETE FROM data")
            conn.commit()
            return {"data": result}
