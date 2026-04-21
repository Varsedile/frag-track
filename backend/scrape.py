from bs4 import BeautifulSoup
import requests
import json

# Scraping functions for each website.

def belvish_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"f-price-item f-price-item--sale text-xl md:text-2xl prod__price text-color-regular-price"})
    price = (spans[0].string.strip())
    return price

def whiffculture_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"price-item price-item--regular"})
    price = (spans[0].string.strip())
    return price

def splashfrag_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"woocommerce-Price-amount amount"})
    price = (spans[0].string.strip())
    return price

def perfumepalace_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("span", attrs={"class":"money bacurr-money"})
    price = (spans[0].string.strip())
    return price

def fragheaven_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spans = soup.find_all("div", attrs={"class":"t4s-product-price"})
    price = (spans[0].string.strip())
    return price

# Reading the JSON file and scraping.

fragfile = json.load(open("backend/fragrances.json"))

num = 0

# for frag in fragfile["perfumes"]:
#     frag_prices = {
#     "fragid" : num,
#     "belvish_price" : belvish_scraping(fragfile["perfumes"][num]["link"]["belvish"]),
#     "whiffculture_price" : whiffculture_scraping(fragfile["perfumes"][num]["link"]["whiffculture"]),
#     "splashfrag_price" : splashfrag_scraping(fragfile["perfumes"][num]["link"]["splashfrag"]),
#     "perfumepalace_price" : perfumepalace_scraping(fragfile["perfumes"][num]["link"]["perfumepalace"]),
#     "fragheaven_price" : fragheaven_scraping(fragfile["perfumes"][num]["link"]["fragheaven"]),
#     }
#     num += 1
