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
    global list_of_dates


    for row in rows:
        #print(row.text,' ')
        #find_date = row.find_all('td', {'class': 'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left'})
        list_of_dates.append(row.text)
        print(row.text)

    return table
#expiramenting how I want to break up the rows of data into appropriate strings
import_table()
print(list_of_dates)
print(len(list_of_dates))
seperated_dates = list_of_dates[3]#[2:5]
print(seperated_dates)

