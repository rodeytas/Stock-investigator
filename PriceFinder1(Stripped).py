import requests
import sys
from bs4 import BeautifulSoup
def scraper(stock):
        print(stock)
        URL='https://finviz.com/quote.ashx?t=' + stock
        print(URL)
        source = requests.get(URL)
        soup = BeautifulSoup(source.content, 'lxml')
        table = soup.findAll('b')
        price = table[71].text
        print('The price for one share is only ' + price + '!')
scraper(str(sys.argv[-1]))

