# test_database.py
import unittest
import os
import database_basics as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_name = "test_db.sqlite"
        self.connection = db.connect_to_database(self.db_name)
        db.create_table(self.connection)

    def tearDown(self):
        self.connection.close()
        os.remove(self.db_name)

    def test_insert_and_retrieve_data(self):
        db.insert_data(self.connection, "Alice", 23)
        db.insert_data(self.connection, "Bob", 25)
        data = db.retrieve_data(self.connection)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0][1], "Alice")
        self.assertEqual(data[1][2], 25)

if __name__ == "__main__":
    unittest.main()

