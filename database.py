import os
import sqlite3

import yaml


DATABASE_FILE = os.path.join('data', 'database.sqlite')
STATEMENTS_FILE = os.path.join('data', 'statements.yml')


class DatabaseHelper(object):
    def __init__(self):
        self._db_connection = None

    def __enter__(self):
        self._db_connection = sqlite3.connect(DATABASE_FILE)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db_connection.close()

    def _create_tables(self):
        """Creates a database from the instructions in `statements.yml`"""
        with open(STATEMENTS_FILE, 'r+') as f:
            statements = yaml.safe_load(f)

        create_statements = statements.get('create', list())

        for s in create_statements:
            self.insert(s)

    def _destroy_tables(self):
        """Deletes the database from the instructions in `statements.yml`"""
        with open(STATEMENTS_FILE, 'r+') as f:
            statements = yaml.safe_load(f)

        destroy_statements = statements.get('destroy', list())

        for s in destroy_statements:
            self.insert(s)

    @property
    def cursor(self):
        """Returns a cursor for this connection"""
        if not self._db_connection:
            self._db_connection = sqlite3.connect(DATABASE_FILE)
        return self._db_connection.cursor()

    def initialize(self):
        """Destroys and reinitializes the database"""
        self._destroy_tables()
        self._create_tables()

        with open(STATEMENTS_FILE, 'r+') as f:
            statements = yaml.safe_load(f)

        initialize_statements = statements.get('initialize', list())

        for s in initialize_statements:
            self.insert(s)

    def select(self, query):
        """Runs the submitted query against the database"""
        print(query)
        cursor = self.cursor
        cursor.execute(query)
        return cursor.fetchall()

    def insert(self, query):
        """Runs the submitted query against the database"""
        print(query)
        cursor = self.cursor
        cursor.executescript(query)
        self._db_connection.commit()

    def select_safe(self, query, params):
        """Runs the submitted query against the database"""
        cursor = self.cursor
        print(query)
        print(params)
        print(type(params))
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def insert_safe(self, query, params):
        """Runs the submitted query against the database"""
        cursor = self.cursor
        print(query)
        print(params)
        print(type(params))
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self._db_connection.commit()
