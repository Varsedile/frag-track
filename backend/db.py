import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS fragrance (id INTEGER PRIMARY KEY, name TEXT, belvish TEXT, whiffculture TEXT, splashfrag TEXT, perfumepalace TEXT, fragheaven TEXT, added_at DATETIME)")
cursor.execute("CREATE TABLE IF NOT EXISTS price_history (id INTEGER PRIMARY KEY, fragrance_id INTEGER, belvish_price REAL, whiffculture_price REAL, splashfrag_price REAL, perfumepalace_price REAL, fragheaven_price REAL, scraped_at DATETIME, FOREIGN KEY(fragrance_id) REFERENCES fragrance(id))")

cursor.execute("INSERT INTO fragrance (name) VALUES (?)", (name,))
