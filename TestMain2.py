import tkinter as tk
window = tk.Tk()

class UserEntry:
    def __init__(self, date, price, entry_num):
        self.date = 0
        self.price = 0
        self.entry_num = 0

list_user_entry = {}

entry_list = []









class Counter:
    def __init__(self):
        self.count = 0

class Price:
    def __init__(self):
        self.price = 0

test_counter = Counter()

# Functions
def date_button():
    global format_date
    user_date = entrystuff.get()
    months = [ 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec' ]
    month_digits = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' ]
    month_seg = user_date[0:2]

    date_seg = user_date[3:5]
    year_seg = user_date[6:10]


    place_holder = month_digits.index(month_seg)
    month_code = months[place_holder]
    format_date = '{} {}, {}'.format(month_code, date_seg, year_seg)
    test_counter.count +=1
    entry_num = 'Entry number {}'.format(test_counter.count)
    if format_date in dates:
        date_index = dates.index(format_date)
        matching_price =  sliced_close_price[date_index]
        list_user_entry.update({format_date:matching_price})




    test_for_date(format_date, entry_num)

def test_for_date(date_string, entry_name):
        name_for = entry_name
        global entry_num
        if date_string in dates:
            date_index = dates.index(date_string)
            matching_price = sliced_close_price[date_index]
            list_user_entry.update({date_string: matching_price})
            name_for = UserEntry(date_string,matching_price,entry_name)
            print(name_for)







#def capture_price(entry_value):









# Wigets
greeting = tk.Label(text = "Welcome to Bitcoin ROI/DCA calculator")

date_label = tk.Label(
    text = "Please enter a past date you would like to buy Bitcoin on\n" "MM/DD/YY",
    fg = "white",
    bg = "black",
    width =50,
    height=3
)
entrystuff = tk.StringVar()

entry_for_date = tk.Entry(
    textvariable = entrystuff,
    bg = "white",
    fg = "black",
    width = 30)


button_for_date = tk.Button(text = "Enter", command = date_button)
#button_for_USD = tk.Button(text = "Enter", command= USD_button)

usd_amt_label = tk.Label(
    text = "Please enter a dollar amount you would like to invest",
    fg = "white",
    bg = "black",
    width = 50,
    height = 3,
)
entry_usd = tk.IntVar()

entry_for_USD = tk.Entry(
    textvariable = entry_usd,
    bg = "white",
    fg = "black",
    width = 30)


# Layout for wigets
greeting.grid(row = 0, column = 0)
date_label.grid(row = 1, column = 0)
entry_for_date.grid(row = 2, column =0)
button_for_date.grid(row = 2, column = 1)
usd_amt_label.grid(row = 3, column = 0)
entry_for_USD.grid(row = 4, column = 0)
#button_for_USD.grid(row = 4, column = 1)

import bs4
import requests
from bs4 import BeautifulSoup
import time


rows_in_table = []
cells_in_table = []
dates = []
sliced_close_price = []
#imported_button_func =


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

def create_entry_list():
    count = 0
    for entry in len(dates):
        count += 1
        cated = 'entry number {}'.format(count)
        entry_list.append(cated)

create_entry_list()





import_table()

extract_close_prices(cells_in_table)
append_master_lists()






window.mainloop()