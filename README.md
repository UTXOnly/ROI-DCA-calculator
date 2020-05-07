# CIS153 Final Project
ROI/DCA calculator for Bitcoin
By Brian Hartford

This is a return on investment/dollar cost averaging calculator for Bitcoin. The user will interact with a graphical user interface, where they will enter a past date they would have purchased Bitcoin on as well as the dollar amount they would have spent. 

The program then scrapes historical price data from CoinMarketCap.com to determine how much Bitcoin the user's money would buy on that particular date. The program then scrapes the current price of Bitcoin and calculates the difference in value denominated in USD.

The program will return the ROI expressed as a percentage and a dollar amount to the GUI. All of the data used in calculations will be exported to a csv file sot he user can save these scenarios and calculate gains if using the dollar cost averaging investment method. 

To use this program enter a date into entry field, then an amount to invest. Press the calculate ROI button, you are encouraged to try out multiple entries. After you have a few entries, press the calculate DCA button to calculate your dollar cost averaging position. When you are done, press the export button to export all of your entries into a csv file.

To run this program you need to install the modules Tkinter, csv, bs4, and requests. You can do that by using the install script. Open a terminal in the same directory and type:

chmod +x install.sh

./install.sh



