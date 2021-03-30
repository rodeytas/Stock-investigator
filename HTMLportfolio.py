import gspread
import requests
import datetime
import time
import sys
import re
from bs4 import BeautifulSoup
now = datetime.datetime.now()
stocks = ['AAPL', 'MSFT']

def portfolio_scraper(stocks):
        portfolio_info = []
        for stock in stocks:
            URL='https://finance.yahoo.com/quote/' + stock
            source = requests.get(URL)
            soup = BeautifulSoup(source.content, 'lxml')
            price = soup.find('span', attrs={"data-reactid": "50"}).text
            price_string = '$' + price
            change = soup.find('span', attrs={"data-reactid": "51"}).text
            changelist = change.split(' ')
            percent_change = changelist[-1].replace('(', '').replace(')', '')
            dollar_change = changelist[0]
            stock = {}
            stock['Price'] = price_string
            stock['Percent Change'] = percent_change
            stock['$ Change'] = dollar_change
            portfolio_info.append(stock)
        portfolio = {stock:info for stock, info in zip(stocks, portfolio_info)}
        print(portfolio)
portfolio_scraper(stocks)
