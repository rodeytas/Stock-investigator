import requests
import datetime
import sys
import re
from bs4 import BeautifulSoup
now = datetime.datetime.now()
stocks = []
company_names = []
prices = []
percent_changes = []
average_volumes = []
volumes_today = []
volume_percents = []
def portfolio_scraper(stocks):
        scrape = open("stocks.txt", "r")
        stocks = scrape.readlines()
        scrape.close()
        for stock in stocks:
                URL='https://finviz.com/quote.ashx?t=' + stock
                source = requests.get(URL)
                soup = BeautifulSoup(source.content, 'lxml')
                table = soup.findAll('b')
                price = table[71].text
                price_string = '$' + price
                percent_change_string = table[77].text
                percent_change = float(percent_change_string[0:-2])
                volume_today_string = table[76].text
                volume_today = int(volume_today_string.replace(',', ''))
                average_volume_string = table[70].text
                if average_volume_string[-1] == 'M':
                        average_volume = float(average_volume_string[0:-2]) * 1000000
                elif average_volume_string[-1] == 'K':
                        average_volume = int(float(average_volume_string[0:-2]) * 1000)
                else:
                        average_volume = average_volume_string
                company_name = soup.find('title').text
                prices.append(price_string)
                percent_changes.append(percent_change_string)
                average_volumes.append(average_volume_string)
                volumes_today.append(volume_today_string)
                company_names.append(company_name)
                volume_percent = str(round((float(float(volume_today)/average_volume) * 100), 2)) + '%'
                volume_percents.append(volume_percent + ' of average volume')
        portfolio = list(zip(stocks, company_names, prices, percent_changes, average_volumes, volumes_today, volume_percents))
        savefile = open("portfolio.txt", "a+")
        savefile.write(str(now))
        savefile.write("\n")
        for asset in portfolio:
                savefile.write(str(asset))
                savefile.write("\n")
        return company_names
portfolio_scraper(stocks)
