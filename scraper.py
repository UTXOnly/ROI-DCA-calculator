import bs4
import requests
from bs4 import BeautifulSoup
import time

rows_in_table = []
cells_in_table = []
sliced_close_price = []


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

    global rows_in_table
    global cells_in_table

    for row in rows:
        if row != rows[0]:
            rows_in_table.append(row.text)
        #print(row.text)
            for cell in row:
                if cell.text != 'Date':
                    cells_in_table.append(cell.text)


def extract_close_prices(list_to_review):
    global list_dates, list_close_price
    list_dates = list_to_review[0:-1:7]
    #print(list_dates)
    list_close_price = list_to_review[4:-1:7]
    #print(list_close_price)
    return list_dates, list_close_price

#expirementing how I want to break up the rows of data into appropriate strings
import_table()
#print(cells_in_table)
extract_close_prices(cells_in_table)
#print(list_dates)
#print(list_close_price)

