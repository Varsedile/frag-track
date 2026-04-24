from bs4 import BeautifulSoup
import requests
import json
import db

# Scraping functions for each website.

def belvish_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"f-price-item f-price-item--sale text-xl md:text-2xl prod__price text-color-regular-price"})
    price = (spans[0].string.replace("Rs.", "").strip())
    return price

def whiffculture_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"price-item price-item--regular"})
    price = (spans[0].string.replace("Rs.", "").strip())
    return price

def aarfrag_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("strong", attrs={"class":"h2 fw-600 text-primary"})
    if len(spans) == 0:
        spans = soup.find_all("strong", attrs={"class":"h3 fw-600 text-primary"})
    price = (spans[0].text.replace("₹", "").strip())
    return price

def perfumepalace_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"product__price on-sale"})
    price = (spans[0].text.replace("Rs.", "").strip())
    return price

def fragheaven_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("div", attrs={"class":"t4s-product-price"})
    price = (spans[0].text.replace("Rs.", "").split(' ', 2)[2].split('\n', 1)[0].strip())
    return price

# Reading the JSON file and scraping.

fragfile = json.load(open("backend/fragrances.json"))

fragprices = []

for frag in fragfile["perfumes"]:
    print("done with " + frag["name"])
    fragprices.append({
    "belvish_price" : belvish_scraping(frag["link"]["belvish"]),
    "whiffculture_price" : whiffculture_scraping(frag["link"]["whiffculture"]),
    "aarfrag_price" : aarfrag_scraping(frag["link"]["aarfrag"]),
    "perfumepalace_price" : perfumepalace_scraping(frag["link"]["perfumepalace"]),
    "fragheaven_price" : fragheaven_scraping(frag["link"]["fragheaven"]),
    })

# Running database functions to add scraped data to the database.

db.setup_database()
db.insert_frags(fragfile)
db.insert_prices(fragprices)