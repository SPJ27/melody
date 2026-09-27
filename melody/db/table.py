import sqlite3

class Database:
    def __init__(self, name='sqlite3'):
        self.db = sqlite3.connect(f'{name}.db')

class Table:
    def __init__(self, connection):
        self.cursor = connection.cursor()

    # Write the SQL command to create the Students table
        create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    '''
        self.cursor.execute(create_table_query)
        connection.commit()
