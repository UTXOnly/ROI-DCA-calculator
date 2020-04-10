import tkinter as tk
window = tk.Tk()



# Functions
def date_button():
    user_date = entry_for_date.get()
    return user_date
    print(user_date)





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


button_for_date = tk.Button(text = "enter", command = date_button)


# Layout for wigets
greeting.grid(row = 0, column = 0)
date_label.grid(row = 1, column = 0)
entry_for_date.grid(row = 2, column =0)
button_for_date.grid(row = 2, column = 1)

date_button()
window.mainloop()
