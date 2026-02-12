import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'localhost'),
            port=int(os.environ.get('MYSQL_PORT', 3306)),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', ''),
            database=os.environ.get('MYSQL_DATABASE', 'bank_db')
        )
        print("✅ Database connection successful!")
        return connection
    except Error as e:
        print(f"❌ Database connection error: {e}")
        return None