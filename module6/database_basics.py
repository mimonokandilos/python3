# database_basics.py
import sqlite3

def connect_to_database(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    connection.commit()

def insert_data(connection, name, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    connection.commit()

def retrieve_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def close_connection(connection):
    connection.close()

if __name__ == "__main__":
    db_name = "student_db.sqlite"
    connection = connect_to_database(db_name)
    create_table(connection)
    insert_data(connection, "Alice", 23)
    insert_data(connection, "Bob", 25)
    data = retrieve_data(connection)
    
    for row in data:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("---")
    
    close_connection(connection)

