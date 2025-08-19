import sqlite3
conn = sqlite3.connect("tinyurl.db")
cursor = conn.cursor()
import base62

cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL UNIQUE,
    code TEXT UNIQUE
)           
""")

conn.commit()

def insert_url(url):
    cursor.execute("INSERT INTO links(url) VALUES (?)" (url))
    conn.commit()
    
    new_id = cursor.lastrowid
    code = base62.encode(new_id)
    
    cursor.execute("UPDATE links SET code = ? WHERE id = ?" (code, new_id))
    conn.commit()

    return code
    

def fetch_by_code(x):
    cursor.execute("SELECT url FROM links WHERE code = ?," (x,))
    row = cursor.fetchone()
    if row:
        return row[0]
    return None

def list_all():
    cursor.execute("SELECT * FROM links")
    return cursor.fetchall()

def delete_by_code(x):
    cursor.execute("DELETE FROM links WHERE code = ?," (x,))
    conn.commit()

