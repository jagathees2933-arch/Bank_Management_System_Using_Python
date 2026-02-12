import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv
load_dotenv()

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=os.environ.get('POSTGRESQL_HOST', 'localhost'),
            port=int(os.environ.get('POSTGRESQL_PORT', 5432)),
            user=os.environ.get('POSTGRESQL_USER', 'postgres'),
            password=os.environ.get('POSTGRESQL_PASSWORD', ''),
            database=os.environ.get('POSTGRESQL_DATABASE', 'bank_db')
        )
        print("✅ Database connection successful!")
        return connection
    except Error as e:
        print(f"❌ Database connection error: {e}")
        return None
