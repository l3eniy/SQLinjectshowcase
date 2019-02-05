from database import DatabaseHelper


def initialize_database():
    """Calls SQL statements to populate the database"""
    with DatabaseHelper() as db:
        db.initialize()
