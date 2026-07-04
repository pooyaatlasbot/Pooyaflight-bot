import sqlite3

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        phone TEXT,
        city TEXT,
        course TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_registration(full_name, phone, city, course):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO registrations(full_name,phone,city,course) VALUES(?,?,?,?)",
        (full_name, phone, city, course)
    )

    conn.commit()
    conn.close()
