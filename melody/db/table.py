from peewee import ModelBase, SqliteDatabase, Model, CharField, IntegerField, BooleanField


class Database:
    current = None

    def __init__(self, name="sqlite3.db"):
        self.db = SqliteDatabase(name)
        Database.current = self

    def register(self, tables):
        self.db.create_tables(tables)


class TableMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        table = super().__new__(cls, name, bases, attrs)

        if Database.current:
            table._meta.database = Database.current.db

        return table


class Table(Model, metaclass=TableMeta):
    pass
