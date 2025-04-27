import os
import sqlite3
from contextlib import contextmanager
from models import transaction

DATABASE = os.getenv("DATABASE", default="finance.db")
SCHEMA = "schema.sql"


@contextmanager
def get_database_connection():
    connection = sqlite3.connect(DATABASE)
    try:
        yield connection
    finally:
        connection.close()


def initialize_database():
    with get_database_connection() as connection:
        with open(SCHEMA, "r") as file:
            sql_script = file.read()
        connection.executescript(sql_script)


class Transaction(transaction.Transaction):
    def send_to_database(self):
        with get_database_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO transactions (date, description, amount) VALUES (?, ?, ?)",
                (self.date, self.description, self.amount),
            )
            connection.commit()
