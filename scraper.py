import bs4
import requests
from bs4 import BeautifulSoup
import time

rows_in_table = []
dates_in_table = []
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

    for row in rows:
        rows_in_table.append(row.text)
        print(row.text)

def slice_dates_from_rows():
    global dates_in_table
    for date in rows_in_table:
        sliced_date = date[0:12]
        dates_in_table.append(sliced_date)

def slice_close_price_from_rows():
    global sliced_close_price
    global rows_in_table
    for close_price in rows_in_table:
        sliced_close = close_price[36:44]
        sliced_close_price.append(sliced_close)

def list_cleaner(list_to_clean):
    del list_to_clean[0:3]



#expirementing how I want to break up the rows of data into appropriate strings
import_table()
slice_dates_from_rows()
slice_close_price_from_rows()
list_cleaner(dates_in_table)
list_cleaner(sliced_close_price)

print(dates_in_table)
print(sliced_close_price)
if 'Apr 07, 2020' in dates_in_table:
    print('This is a valid date')

