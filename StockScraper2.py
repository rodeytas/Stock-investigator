import time
import requests
import sys
import pandas as pd
import progressbar as progressbar
from bs4 import BeautifulSoup
def scraper(stock):
        print(stock)
        ticker = stock
        out=[]
        URL='https://finviz.com/quote.ashx?t='+stock
        source = requests.get('https://finviz.com/quote.ashx?t=' + stock)
        soup = BeautifulSoup(source.content, 'lxml')
        print(URL)
        table = soup.find_all(lambda tag: tag.name=='table')
        rows = table[3].find_all(lambda tag: tag.name=='tr')
        for i in range(len(rows)):
                td=rows[i].find_all(lambda tag: tag.name=='td')
                out=out+[x.text for x in td]

        ls=['Ticker']+out[::2]
        
        dict_ls={k:ls[k] for k in range(len(ls))}
        df=pd.DataFrame()
        p = progressbar.ProgressBar()
        p.start()
        for j in range(len(ls)):
                p.update(j/len(ls) * 100)
                source = requests.get("https://finviz.com/quote.ashx?t="+ls[j])
                if source.status_code !=200:
                    continue
                soup = BeautifulSoup(source.content, 'lxml')
                table = soup.find_all(lambda tag: tag.name=='table')
                rows = table[3].findAll(lambda tag: tag.name=='tr')
                out=[]
                for i in range(len(rows)):
                    td=rows[i].find_all('td')
                    out=out+[x.text for x in td]
                out=[ls[j]]+out[1::2]
                out_df=pd.DataFrame(out).transpose()
                df=df.append(out_df,ignore_index=True)

        p.finish()
        df=df.rename(columns=dict_ls)  
        print(df)
        return(df)

scraper(str(sys.argv))        
