import os
import sqlite3

import yaml


DATABASE_FILE = 'database.sqlite'
STATEMENTS_FILE = 'statements.yml'


class DatabaseHelper(object):
    def __init__(self):
        self._db = None

    def __enter__(self):
        self._create_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db.close()

    def _create_database(self):
        """Creates a database from the instructions in `statements.yml`"""
        self._db = sqlite3.connect(os.path.join('data', DATABASE_FILE))

        with open(os.path.join('data', STATEMENTS_FILE), 'r+') as f:
            statements = yaml.safe_load(f)

        create_statements = statements.get('create', list())

        for s in create_statements:
            self._db.execute(s)

    def _destroy_database(self):
        """Deletes the database from the instructions in `statements.yml`"""
        with open(os.path.join('data', STATEMENTS_FILE), 'r+') as f:
            statements = yaml.safe_load(f)

        destroy_statements = statements.get('destroy', list())

        for s in destroy_statements:
            self._db.execute(s)

        self._db = None

    @property
    def database(self):
        """

        :return:
        """
        if not self._db:
            self._create_database()
        return self._db

    def restart(self):
        """Destroys and reinitializes the database"""
        self._destroy_database()
        self._create_database()

        with open(os.path.join('data', STATEMENTS_FILE), 'r+') as f:
            statements = yaml.safe_load(f)

        initialize_statements = statements.get('initialize', list())

        for s in initialize_statements:
            self._db.execute(s)
