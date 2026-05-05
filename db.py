import json
import datetime
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
conn = psycopg2.connect(DATABASE_URL)

# Importing json data.
fragfile = json.load(open("fragrances.json"))

# Database setup for adding scraped data.
cursor = conn.cursor()

def setup_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS fragrance (id SERIAL PRIMARY KEY, name TEXT UNIQUE, belvish TEXT, whiffculture TEXT, aarfrag TEXT, perfumepalace TEXT, fragheaven TEXT, added_at TIMESTAMP)")
    cursor.execute("CREATE TABLE IF NOT EXISTS price_history (id SERIAL PRIMARY KEY, fragrance_id INTEGER, belvish_price FLOAT, whiffculture_price FLOAT, aarfrag_price FLOAT, perfumepalace_price FLOAT, fragheaven_price FLOAT, scraped_at TIMESTAMP, FOREIGN KEY(fragrance_id) REFERENCES fragrance(id))")

# Adding scraped data to the database.
def insert_frags(fragfile):
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT INTO fragrance (name, belvish, whiffculture, aarfrag, perfumepalace, fragheaven, added_at) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (frag["name"], frag["link"]["belvish"], frag["link"]["whiffculture"], frag["link"]["aarfrag"], frag["link"]["perfumepalace"], frag["link"]["fragheaven"], datetime.datetime.now()))
        conn.commit()

def insert_prices(fragprices):
    num = 0
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT INTO price_history (fragrance_id, belvish_price, whiffculture_price, aarfrag_price, perfumepalace_price, fragheaven_price, scraped_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", (num + 1, fragprices[num]["belvish_price"], fragprices[num]["whiffculture_price"], fragprices[num]["aarfrag_price"], fragprices[num]["perfumepalace_price"], fragprices[num]["fragheaven_price"], datetime.datetime.now()))
        conn.commit()
        num += 1

# Querying databases for frontend
def get_all_fragrances():
    cursor.execute("SELECT DISTINCT ON (fragrance.id) * FROM fragrance LEFT JOIN price_history ON fragrance.id = price_history.fragrance_id ORDER BY fragrance.id, scraped_at DESC")
    fragrances = cursor.fetchall()
    return fragrances

def get_one_fragrance(id):
    cursor.execute("SELECT * FROM fragrance LEFT JOIN price_history ON fragrance.id = price_history.fragrance_id WHERE fragrance.id = %s", (id,))
    fragrance = cursor.fetchall()
    return fragrance

def get_price_history(id):
    cursor.execute("SELECT * FROM price_history WHERE price_history.fragrance_id = %s", (id,))
    fragrance = cursor.fetchall()
    return fragrance