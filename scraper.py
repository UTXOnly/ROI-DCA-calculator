import bs4
import requests
import re
from bs4 import BeautifulSoup


rows_in_table = []
cells_in_table = []
dates = []
sliced_close_price = []
real_close_price = []

class RegexStuff():
    def  __init__(self):
        self.pattern = "[,]"
        self.pattern2 = "[a-zA-Z]"

regextool = RegexStuff()


def parsePrice():
    r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    # price = soup.find('div', {'class': 'cmc-details-panel-price__price'})
    price = soup.find_all('div', {'class': 'cmc-details-panel-price jta9t4-0 fcilTk'})[0].find('span').text
    return price

def import_table():
    r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20200506')
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    table = soup.find('div', {'class': 'cmc-tab-historical-data ctxmt9-0 ASvFA'})
    rows = table.find_all('tr')

    global rows_in_table
    global cells_in_table
    global seperated_cells

    for row in rows:
        if row != rows[0]:
            rows_in_table.append(row.text)


            for cell in row:

                if cell.text != 'Date':
                    cells_in_table.append(cell.text)




                    """if (re.search(regextool.pattern, cell.text)):
                        print(cell.text)
                        
                        
                    else:
                        break"""



def extract_close_prices(list_to_review):
    global list_dates, list_close_price, dates, sliced_close_price
    list_dates = list_to_review[0:-1:7]

    dates.append(list_dates)
    list_close_price = list_to_review[4:-1:7]



    sliced_close_price.append(list_close_price)


    return list_dates, list_close_price

def append_master_lists():
    global list_dates, list_close_price
    for date in list_dates:
        dates.append(date)
    for price in list_close_price:
        sliced_close_price.append(price)

def get_close_price(list_to_review):
    date = list_to_review.pop(0)
    date2 = list_to_review.pop(0)
    date3 = list_to_review.pop(0)
    date4= list_to_review.pop(0)
    close = list_to_review[0:-1:7]

    """print(close)
    print(cells_in_table)"""
    real_close_price.append(close)
    #print(real_close_price)
i = 0
def close_price_to_float(list_to_review):
    for cell in list_to_review:
        global i
        for cell2 in cell:

            if re.search(regextool.pattern, cell2) and cell2 != cell[-1]:



                split = cell[i].split(',')
                joined = split[0] + split[1]
                price_float = float(joined)
                print(price_float)

            else:
                break
            i += 1
        """single_element = float(cell[i])
        print(single_element)"""

    """for price in list_close_price:
        split = price.split(',')
        joined = split[0] + split[1]
        price_float = float(joined)
        sliced_close_price.append(price_float)"""





import_table()

extract_close_prices(cells_in_table)
append_master_lists()
get_close_price(cells_in_table)
close_price_to_float(real_close_price)



#formatted_date = date_button()
#print(formatted_date)
