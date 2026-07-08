from bs4 import BeautifulSoup
import requests
import json
import db
import urllib.robotparser as urobot
import random

def test_scraping(link):
    return random.randint(3000, 6000)

# Scraping functions for each website.

def website_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    if "belvish.com" in link:
        spans = soup.find_all("span", attrs={"class":"f-price-item f-price-item--sale text-xl md:text-2xl prod__price text-color-regular-price"})
        try:
            price = (spans[0].string.replace("Rs.", "").replace(",", "").replace(".", "").strip())
            return price
        except:
            return None
    if "whiffculture.com" in link:
        spans = soup.find_all("span", attrs={"class":"price-item price-item--regular"})
        try:
            price = (spans[0].string.replace("Rs.", "").replace(",", "").replace(".", "").strip())
            return price
        except:
            return None
    if "aarfragrances.com" in link:
        spans = soup.find_all("strong", attrs={"class":"h2 fw-600 text-primary"})
        if len(spans) == 0:
            spans = soup.find_all("strong", attrs={"class":"h3 fw-600 text-primary"})
        try:
            price = (spans[0].text.replace("₹", "").replace(",", "").replace(".", "").strip())
            return price
        except:
            None
    if "perfumepalace.com" in link:
        spans = soup.find_all("span", attrs={"class":"product__price on-sale"})
        try:
            price = (spans[0].text.replace("Rs.", "").replace(",", "").replace(".", "").strip())
            return price
        except:
            return None
    if "fragranceheaven.com" in link:
        spans = soup.find_all("div", attrs={"class":"t4s-product-price"})
        try:
            price = (spans[0].text.replace("Rs.", "").replace(",", "").split(' ', 2)[2].split('\n', 1)[0].replace(".", "").strip())
            return price
        except:
            return None

# Robots checker for each website

def check_robots(robots):
    dealers = json.load(open("dealers.json"))
    for dealer in dealers["websites"]:
        URL = dealer["link"] + "/robots.txt"
        response = requests.get(URL)
        text = response.text
        lines = text.splitlines()
        rp = urobot.RobotFileParser()
        rp.parse(lines)
        if rp.can_fetch("*", dealer["product-page"]): 
            robots.update({dealer["name"]: True})
        else:
            robots.update({dealer["name"]: False})

# Reading the JSON file and scraping.
def run_scraping():
    # Initializing and checking robots
    fragfile = json.load(open("fragrances.json"))
    dealerfile = json.load(open("dealers.json"))
    fragprices = []
    # robots = {}
    # check_robots(robots)

    for frag in fragfile["perfumes"]:
        for dealer in dealerfile["websites"]:
            fragprices.append({
            "name" : frag["name"],
            "website" : dealer["name"],
            "price" : test_scraping(frag["link"][dealer["name"]]) # if robots[dealer["name"]] else None
            })

    # Running database functions to setup databases.
    db.setup_database()
    db.insert_values(fragprices)
