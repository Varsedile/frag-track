import sqlite3
import json
import datetime

# Importing json data.

fragfile = json.load(open("fragrances.json"))

# Database setup for adding scraped data.

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

def setup_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS fragrance (id INTEGER PRIMARY KEY, name TEXT, belvish TEXT, whiffculture TEXT, aarfrag TEXT, perfumepalace TEXT, fragheaven TEXT, added_at DATETIME)")
    cursor.execute("CREATE TABLE IF NOT EXISTS price_history (id INTEGER PRIMARY KEY, fragrance_id INTEGER, belvish_price REAL, whiffculture_price REAL, aarfrag_price REAL, perfumepalace_price REAL, fragheaven_price REAL, scraped_at DATETIME, FOREIGN KEY(fragrance_id) REFERENCES fragrance(id))")

# Adding scraped data to the database.

def insert_frags(fragfile):
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT INTO fragrance (name, belvish, whiffculture, aarfrag, perfumepalace, fragheaven, added_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (frag["name"], frag["link"]["belvish"], frag["link"]["whiffculture"], frag["link"]["aarfrag"], frag["link"]["perfumepalace"], frag["link"]["fragheaven"], datetime.datetime.now()))
        conn.commit()

def insert_prices(fragprices):
    num = 0
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT INTO price_history (fragrance_id, belvish_price, whiffculture_price, aarfrag_price, perfumepalace_price, fragheaven_price, scraped_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (num + 1, fragprices[num]["belvish_price"], fragprices[num]["whiffculture_price"], fragprices[num]["aarfrag_price"], fragprices[num]["perfumepalace_price"], fragprices[num]["fragheaven_price"], datetime.datetime.now()))
        conn.commit()
        num += 1

def get_all_fragrances():
    cursor.execute("SELECT * FROM fragrance LEFT JOIN price_history ON fragrance.id = price_history.fragrance_id GROUP BY fragrance_id")
    fragrances = cursor.fetchall()
    return fragrances
