import bs4
import requests
from bs4 import BeautifulSoup
import time

list_of_dates = []

def parsePrice():
    r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    # price = soup.find('div', {'class': 'cmc-details-panel-price__price'})
    price = soup.find_all('div', {'class': 'cmc-details-panel-price jta9t4-0 fcilTk'})[0].find('span').text
    return price

def import_table():
    r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    table = soup.find('div', {'class': 'cmc-tab-historical-data ctxmt9-0 ASvFA'})
    rows = table.find_all('tr')
    for row in rows:
        print(row.text,' ')
        find_date = row.find_all('td', {'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left'})
        print(len(find_date))
        """date_finder = find_date.find('div')
        print(date_finder.text)
        for items in row:
            print(items.text)"""
    return table

import_table()

