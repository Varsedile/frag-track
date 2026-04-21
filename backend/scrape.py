from bs4 import BeautifulSoup
import requests
import json

# Scraping functions for each website.

def belvish_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    prices = soup.find_all("span", attrs={"class":"f-price-item f-price-item--sale text-xl md:text-2xl prod__price text-color-regular-price"})
    return prices

def whiffculture_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    prices = soup.find_all("span", attrs={"class":"price-item price-item--regular"})
    return prices

def splashfrag_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    prices = soup.find_all("span", attrs={"class":"woocommerce-Price-amount amount"})
    return prices

def perfumepalace_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    prices = soup.find_all("span", attrs={"class":"money bacurr-money"})
    return prices

def fragheaven_scraping(link):
    page_to_scrape = requests.get(link)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    prices = soup.find_all("div", attrs={"class":"t4s-product-price"})
    return prices  

# Reading the JSON file.

fragfile = json.load(open("backend/fragrances.json"))

print (fragfile["perfumes"][0]["link"]["belvish"])







""" fragNames = []
belvishPrices = []

data = {'name':fragNames, 'belvish_price':belvishPrices}

for name, price in zip(names, prices):
    fragNames.append(name.text)

    clean_price = price.text.replace('\n', '')
    belvishPrices.append(clean_price)

df = pd.DataFrame(data)

print(df) """