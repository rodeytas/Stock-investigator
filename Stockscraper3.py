import requests
import sys
from bs4 import BeautifulSoup
def scraper(stock):
        print(stock)
        counter = 0
        ticker = stock
        URL='https://finviz.com/quote.ashx?t=' + stock
        print(URL)
        source = requests.get(URL)
        soup = BeautifulSoup(source.content, 'lxml')
        soup.prettify()
        table = soup.findAll('b')
        price = table[71]
        print(price)
        #price=table[].findAll('tr')
        #print(price)
scraper(str(sys.argv[-1]))
