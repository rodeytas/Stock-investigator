import gspread
import requests
import datetime
import time
import sys
import re
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
now = datetime.datetime.now()

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/terry/code/Stock-Investigator/PortfolioCredentials")
client = gspread.authorize(creds)
sheet = client.open("Portfolio").sheet1
data = sheet.col_values(1)


def portfolio_scraper(stocks, ss):
        portfolio_info = []
        for stock in stocks:

            #Naming the URL string
            URL='https://finance.yahoo.com/quote/' + stock

            #accessing the URL using BeuatifulSoup
            source = requests.get(URL)
            soup = BeautifulSoup(source.content, 'lxml')

            #Acquiring the information using BeautifulSoup's "find" feature
            price = soup.find('span', attrs={"data-reactid": "50"}).text
            change = soup.find('span', attrs={"data-reactid": "51"}).text
            changelist = change.split(' ')
            percent_change = changelist[-1].replace('(', '').replace(')', '')
            dollar_change = changelist[0]

            #Creating the stock dictionary object
            stock = {}
            stock['Price'] = price_string
            stock['Percent Change'] = percent_change
            stock['$ Change'] = dollar_change

            #Adding the stock to the preliminary list
            portfolio_info.append(stock)

            #This is for locating the areas of the google sheet where the data is going to be stored.
            gs_ticker_location = ss.find(stock)
            gs_dollar_value = ss.cell(gs_ticker_location.row, gs_ticker_location.col + 1)
            gs_dollar_change = ss.cell(gs_ticker_location.row, gs_ticker_location.col + 2)
            gs_percent_change = ss.cell(gs_ticker_location.row, gs_ticker_location.col + 3)

            #Updating the information in the google sheet
            ss.update(gs_dollar_value, price)
            ss.update(gs_dollar_change, dollar_change)
            ss.update(gs_percent_change, percent_change)
            
        #Creating the entire portfolio as standard input (incase you want to use this in another program) (This is as a dictionary)
        portfolio = {stock:info for stock, info in zip(stocks, portfolio_info)}
        return portfolio
portfolio_scraper(data, sheet)

