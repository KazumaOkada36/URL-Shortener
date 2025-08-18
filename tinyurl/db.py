import sqlite3
conn = sqlite3.connect("tinyurl.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    URL TEXT NOT NULL UNIQUE,
    code TEXT UNIQUE
)           
""")

conn.commit()

def insert_URL(URL):
    cursor.execute("""
    INSERT INTO links(URL);
    """)
    conn.commit()
    return id
    

def fetch_by_code(x):
    cursor.execute("""
    SELECT URL FROM links WHERE code = x;               
    """)
    return URL

def list_all():
    cursor.execute("""
    SELECT * FROM links;             
    """)

def delete_by_code(x):
    cursor.execute("""
    DELETE FROM links WHERE code = x;               
    """)
    conn.commit()

