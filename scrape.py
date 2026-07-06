from bs4 import BeautifulSoup
import requests
import json
import db
import urllib.robotparser as urobot

# Scraping functions for each website.

def belvish_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"f-price-item f-price-item--sale text-xl md:text-2xl prod__price text-color-regular-price"})
    try:
        price = (spans[0].string.replace("Rs.", "").replace(",", "").strip())
        return price
    except:
        return None

def whiffculture_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"price-item price-item--regular"})
    try:
        price = (spans[0].string.replace("Rs.", "").replace(",", "").strip())
        return price
    except:
        return None

def aarfrag_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("strong", attrs={"class":"h2 fw-600 text-primary"})
    if len(spans) == 0:
        spans = soup.find_all("strong", attrs={"class":"h3 fw-600 text-primary"})
    try:
        price = (spans[0].text.replace("₹", "").replace(",", "").strip())
        return price
    except:
        None

def perfumepalace_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"product__price on-sale"})
    try:
        price = (spans[0].text.replace("Rs.", "").replace(",", "").strip())
        return price
    except:
        return None

def fragheaven_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("div", attrs={"class":"t4s-product-price"})
    try:
        price = (spans[0].text.replace("Rs.", "").replace(",", "").split(' ', 2)[2].split('\n', 1)[0].strip())
        return price
    except:
        return None
    
def check_robots(robots):
    rp = urobot.RobotFileParser()
    dealers = json.load(open("dealers.json"))
    for dealer in dealers["websites"]:
        URL = dealer["link"] + "/robots.txt"
        response = requests.get(URL)
        text = response.text
        lines = text.splitlines()
        rp.parse(lines)
        if rp.can_fetch("*", dealer["product-page"]): 
            robots.update({dealer["name"]: True})
        else:
            robots.update({dealer["name"]: False})

# Reading the JSON file and scraping.
def run_scraping():
    fragfile = json.load(open("fragrances.json"))
    fragprices = []
    robots = {}
    check_robots(robots)
    print(robots)
    for frag in fragfile["perfumes"]:
        fragprices.append({
        "belvish_price" : belvish_scraping(frag["link"]["belvish"]) if robots["belvish"] else None,
        "whiffculture_price" : whiffculture_scraping(frag["link"]["whiffculture"]) if robots["whiffculture"] else None,
        "aarfrag_price" : aarfrag_scraping(frag["link"]["aarfrag"]) if robots["aarfrag"] else None,
        "perfumepalace_price" : perfumepalace_scraping(frag["link"]["perfumepalace"]) if robots["perfumepalace"] else None,
        "fragheaven_price" : fragheaven_scraping(frag["link"]["fragheaven"]) if robots["fragheaven"] else None,
        })

    # Running database functions to add scraped data to the database.
    db.setup_database()
    db.insert_frags(fragfile)
    db.insert_prices(fragprices)
