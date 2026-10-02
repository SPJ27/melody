import sqlite3

class Database:
    def __init__(self, name='sqlite3'):
        self.db = sqlite3.connect(f'{name}.db')

class Table:
    connection = None
    table_name = None
    columns = {}

    @classmethod
    def create(cls):
        
        columns = ['id INTEGER PRIMARY KEY AUTOINCREMENT']
        for field, field_type in cls.columns.items():
            sql_type = {
                str: 'TEXT',
                int: 'INTEGER',
                float: 'REAL',
                bool: 'BOOL'
            }.get(field_type, 'TEXT')
            columns.append(f'{field} {sql_type}')
        query = f'''
                CREATE TABLE IF NOT EXISTS {cls.table} (
                {columns.join(', ')}
            );
        
                '''
        
        
