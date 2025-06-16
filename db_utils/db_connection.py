import logging

logging.basicConfig(
    filename='logs/db_comparison.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

import sqlite3

def connect_db(db_path):
    """
    Connects to the given SQLite database file.
    Args:
        db_path (str): Path to the SQLite database file
    Returns:
        sqlite3.Connection object
    """
    print("Testing 123")
    print("testing git email")
    return sqlite3.connect(db_path)
