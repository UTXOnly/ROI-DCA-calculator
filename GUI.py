import tkinter as tk
window = tk.Tk()

class UserEntry:
    def __init__(self):
        self.date = 0
        self.price = 0

user_entry1 = UserEntry()

# Functions
def date_button():
    global format_date
    user_date = entry_for_date.get()
    months = [ 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec' ]
    month_digits = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' ]
    month_seg = user_date[0:2]

    date_seg = user_date[3:5]
    year_seg = user_date[6:10]
    """print(date_seg)
    print(year_seg)"""

    place_holder = month_digits.index(month_seg)
    month_code = months[place_holder]
    format_date = '{} {}, {}'.format(month_code, date_seg, year_seg)

    user_entry1.date = format_date
    #print(format_date)
    return format_date, user_entry1




def USD_button():
    USD_amount = entry_for_USD.get()
    print(USD_amount)
    return USD_amount





# Wigets
greeting = tk.Label(text = "Welcome to Bitcoin ROI/DCA calculator")

date_label = tk.Label(
    text = "Please enter a past date you would like to buy Bitcoin on\n" "MM/DD/YY",
    fg = "white",
    bg = "black",
    width =50,
    height=3
)

entry_for_date = tk.Entry(
    bg = "white",
    fg = "black",
    width = 30)


button_for_date = tk.Button(text = "Enter", command = date_button)
button_for_USD = tk.Button(text = "Enter", command= USD_button)

usd_amt_label = tk.Label(
    text = "Please enter a dollar amount you would like to invest",
    fg = "white",
    bg = "black",
    width = 50,
    height = 3,
)

entry_for_USD = tk.Entry(
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
button_for_USD.grid(row = 4, column = 1)






window.mainloop()
