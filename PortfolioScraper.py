import requests
import re
import sys
from bs4 import BeautifulSoup
stocks = ['ACB', 'APHA', 'AUY', 'SBUX']
S_CN_P_AV = []
S_CN_P_AV_VT = []
company_names = []
prices = []
percent_changes = []
average_volumes = []
volumes_today =[]
def portfolio_scraper(stocks):
        for stock in stocks:
                URL='https://finviz.com/quote.ashx?t=' + stock
                source = requests.get(URL)
                soup = BeautifulSoup(source.content, 'lxml')
                table = soup.findAll('b')
                price = table[71].text
                percent_change = table[77].text
                average_volume = table[70].text
                volume_today = table[76].text
                company_name = soup.find('title').text
                print('_______________________________')
                print(company_name)
                print(URL)
                print(stock.upper())
                print('On an average day, this stock is traded ' + average_volume + ' times.')
                print('So far, this stock has traded ' + volume_today + ' times today.')
                print('The price for one share is $' + price + '.')
                print('There has been a ' + percent_change + ' change today.')
portfolio_scraper(stocks)
