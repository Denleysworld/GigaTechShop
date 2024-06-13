import sqlite3

DATABASE_NAME = 'gigatech.db'


conn = sqlite3.connect(DATABASE_NAME)

cursor = conn.cursor()

print("Connected to the database successfully")


def close_connection():
    conn.close()
    print("Database connection closed")
