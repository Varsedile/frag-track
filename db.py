import libsql as sqlite3
import os
import json
import datetime
from dotenv import load_dotenv

load_dotenv()

# Connecting cloud database.

conn = sqlite3.connect(
    database=os.environ["TURSO_DATABASE_URL"],
    auth_token=os.environ["TURSO_AUTH_TOKEN"]
)

# Importing json data.

fragfile = json.load(open("fragrances.json"))

# conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()
cursor1 = conn.cursor()
cursor2 = conn.cursor()

# Database setup for adding scraped data.

def setup_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS fragrance (id INTEGER PRIMARY KEY, name TEXT UNIQUE, belvish TEXT, whiffculture TEXT, aarfrag TEXT, perfumepalace TEXT, fragheaven TEXT, added_at DATETIME)")
    cursor.execute("CREATE TABLE IF NOT EXISTS price_history (id INTEGER PRIMARY KEY, fragrance_id INTEGER, belvish_price REAL, whiffculture_price REAL, aarfrag_price REAL, perfumepalace_price REAL, fragheaven_price REAL, scraped_at DATETIME, FOREIGN KEY(fragrance_id) REFERENCES fragrance(id))")

# Adding scraped data to the database.

def insert_frags(fragfile):
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT OR IGNORE INTO fragrance (name, belvish, whiffculture, aarfrag, perfumepalace, fragheaven, added_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (frag["name"], frag["link"]["belvish"], frag["link"]["whiffculture"], frag["link"]["aarfrag"], frag["link"]["perfumepalace"], frag["link"]["fragheaven"], datetime.datetime.now()))
        conn.commit()
        conn.close()

def insert_prices(fragprices):
    num = 0
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT INTO price_history (fragrance_id, belvish_price, whiffculture_price, aarfrag_price, perfumepalace_price, fragheaven_price, scraped_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (num + 1, fragprices[num]["belvish_price"], fragprices[num]["whiffculture_price"], fragprices[num]["aarfrag_price"], fragprices[num]["perfumepalace_price"], fragprices[num]["fragheaven_price"], datetime.datetime.now()))
        conn.commit()
        conn.close()
        num += 1

# Querying databases for frontend

def get_all_fragrances():
    cursor.execute("SELECT * FROM fragrance LEFT JOIN price_history ON fragrance.id = price_history.fragrance_id GROUP BY fragrance_id")
    fragrances = cursor.fetchall()
    return fragrances

def get_one_fragrance(id):
    cursor1.execute(f"SELECT * FROM fragrance LEFT JOIN price_history ON fragrance.id = price_history.fragrance_id WHERE fragrance.id = {id}")
    fragrance = cursor1.fetchall()
    return fragrance

def get_price_history(id):
    cursor2.execute(f"SELECT * FROM price_history WHERE price_history.fragrance_id = {id}")
    fragrance = cursor2.fetchall()
    return fragrance