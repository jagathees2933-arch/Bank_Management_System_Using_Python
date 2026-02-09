import mysql.connector
from mysql.connector import Error


def get_db_connection():
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',                # Change to your MySQL username
            password='tiger',   # Change to your MySQL password
            database='bank_management'
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        return None