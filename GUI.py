import tkinter as tk
window = tk.Tk()



# Functions
def date_button():
    user_date = entry_for_date.get()
    print(user_date)
    return user_date

def USD_button():
    USD_amount = entry_for_USD.get()
    return USD_amount





# Wigets
greeting = tk.Label(text = "Welcome to Bitcoin ROI/DCA calculator")

date_label = tk.Label(
    text = "Please enter a past date you would like to buy Bitcoin on\n" "ex. April 6, 2020",
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
