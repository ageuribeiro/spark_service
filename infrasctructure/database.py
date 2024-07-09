import sqlite3

def get_db_connection():
    conn  = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS person(
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     age INTEGER NOT NULL
                     )
        ''')
    conn.close()
    