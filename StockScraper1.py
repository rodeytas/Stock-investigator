import requests
import sys
from bs4 import BeautifulSoup
def scraper(stock):
        print(stock)
        ticker = stock
        source = requests.get('https://finance.yahoo.com/quote/' + ticker).text
        soup = BeautifulSoup(source, 'lxml')
        price = soup.find('div', class_='D(ib)').text
        print(price)
scraper(str(sys.argv))

