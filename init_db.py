import psycopg2

# Database connection
conn = psycopg2.connect(
    database="your_database",
    user="your_user",
    password="your_password",
    host="127.0.0.1",
    port="5432"
)
cursor = conn.cursor()

# Create table example
cursor.execute("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) CHECK (role IN ('admin', 'user'))
);
""")

# Remember to close the connection
conn.commit()
cursor.close()
conn.close()