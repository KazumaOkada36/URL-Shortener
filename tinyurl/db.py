import sqlite3

import base62


DB_PATH = "tinyurl.db"

with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL UNIQUE,
        code TEXT UNIQUE
    )           
    """)

def insert_url(url):  
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO links(url) VALUES (?)", (url,))
            new_id = cur.lastrowid
            if not new_id:
                raise RuntimeError("insert failed")   
            code = base62.encode(new_id)
            cur.execute("UPDATE links SET code = ? WHERE id = ?", (code, new_id))
            return code
    except sqlite3.IntegrityError:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT code, id FROM links WHERE url = ?", (url,))
            row = cur.fetchone()
            return row[0]
    

def fetch_by_code(x):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT url FROM links WHERE code = ?", (x,))
        row = cur.fetchone()
        if row:
            return row[0]
        return None

def list_all():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM links")
        return cur.fetchall()

def delete_by_code(x):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM links WHERE code = ?", (x,))

