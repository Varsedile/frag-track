import json
import datetime
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os

project_root = os.path.dirname(os.path.dirname(__file__))

# Load environment variables from .env
load_dotenv()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to the database
conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = True

# Importing json data
fragfile = json.load(open(os.path.join(project_root, "data", "fragrances.json")))
dealerfile = json.load(open(os.path.join(project_root, "data", "dealers.json")))

# Database setup for adding scraped data

def setup_database():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS fragrance (id SERIAL PRIMARY KEY, name TEXT UNIQUE, added_at TIMESTAMP)")
    cursor.execute("CREATE TABLE IF NOT EXISTS fragrance_link (id SERIAL PRIMARY KEY, fragrance_id INT, site_name TEXT, url TEXT, FOREIGN KEY(fragrance_id) REFERENCES fragrance(id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS price_history (id SERIAL PRIMARY KEY, fragrance_id INT, site_name TEXT, price INT, status VARCHAR(10), scraped_at TIMESTAMP, FOREIGN KEY(fragrance_id) REFERENCES fragrance(id))")

# Inserting values into the database

def insert_values(fragprices):
    cursor = conn.cursor()
    for frag in fragfile["perfumes"]:
        cursor.execute("INSERT INTO fragrance (name, added_at) VALUES (%s, %s) ON CONFLICT DO NOTHING", (frag["name"], datetime.datetime.now()))
        for dealer in dealerfile["websites"]:
            cursor.execute("INSERT INTO fragrance_link (fragrance_id, site_name, url) VALUES ((SELECT id FROM fragrance WHERE name = %s), %s, %s) ON CONFLICT DO NOTHING", (frag["name"], dealer["name"], frag["link"][dealer["name"]]))
            cursor.execute("INSERT INTO price_history (fragrance_id, site_name, price, status, scraped_at) VALUES ((SELECT id FROM fragrance WHERE name = %s), %s, %s, %s, %s)", (frag["name"], dealer["name"], [prices["price"] for prices in fragprices if dealer["name"] == prices["website"]][0], ["ok" if prices["price"] != None else "failed" for prices in fragprices][0], datetime.datetime.now()))

# Querying databases for frontend
def get_all_fragrances():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT DISTINCT ON (fragrance.id) * FROM fragrance LEFT JOIN price_history ON fragrance.id = price_history.fragrance_id ORDER BY fragrance.id, scraped_at DESC")
    fragrances = cursor.fetchall()
    return fragrances

def get_one_fragrance(id):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("""
                    WITH info AS (
                    SELECT fragrance.id, name, site_name, price, scraped_at
                    FROM fragrance
                    LEFT JOIN price_history
                    ON fragrance.id = price_history.fragrance_id
                    WHERE fragrance.id = %s)
                   
                    SELECT DISTINCT ON (site_name) info.id, name, info.site_name, price, scraped_at, url
                    FROM info
                    LEFT JOIN fragrance_link
                    ON info.id = fragrance_link.fragrance_id
                    AND info.site_name = fragrance_link.site_name
                    ORDER BY site_name, scraped_at DESC
                """, (id,))
    fragrance = cursor.fetchall()
    return fragrance

def get_price_history(id):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM price_history WHERE price_history.fragrance_id = %s", (id,))
    fragrance = cursor.fetchall()
    return fragrance