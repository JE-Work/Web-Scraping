#!/usr/bin/env python3

#
# This project entailed scraping a site for all tickers and names, for ETF's, 
# Equities, Funds, and Crypto from a financial website.
# The values were to be saved to a CSV file.
# I put together a POC scraping for all the Crypto names and symbols, as well
# as all ETF names and symbols.
#

from bs4 import BeautifulSoup
import csv
import requests
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) \
        AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
}

session = requests.Session()

# URLS
# CRYPTO SCREENER URL
#URL = 'https://finance.example.com/cryptocurrencies/?.tsrc=fin-srch&count=100&offset='
# ETF SCREENER URL
#URL = 'https://finance.example.com/screener/unsaved/2bd325f6-7042-4bbc-977c-0cd546607e19?&count=100&offset=0'


def site_scrape(url):
    try:
        website = session.get(url, headers=HEADERS, timeout=10)
        website.raise_for_status()
        soup = BeautifulSoup(website.text, 'lxml')
    except requests.exceptions.HTTPError as e:
        raise Exception (e)
    except requests.exceptions.Timeout as e:
        raise Exception (e)
    return soup


def scrape(url):
    
    soup = site_scrape(url)
    table = soup.find('div',id='scr-res-table')
    rows = table.find_all('a')
    titles = [row.get('title') for row in rows if row.get('title') is not None]
    names = [row.get_text() for row in rows if row.get_text() != ""]

    with open('ETFs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows(zip(names, titles))


def main():

    for i in range (0, 500, 100):
        url = URL + str(i)
        site_scrape(url)
        scrape(url)
        time.sleep(1)

if __name__ == '__main__':
    main()
