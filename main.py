import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    WIKI_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    resp = requests.get(WIKI_URL)
    soup = bs.BeautifulSoup(resp.text,'lxml')
    table = soup.find('table',id='constituents')

    tickers= []

    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.rstrip("\n")
        tickers.append(ticker)

    print(tickers)

    return tickers

tickers = save_sp500_tickers()

#saves tickers in binary
with open("sp500tickers.picke","wb") as file:
        pickle.dump(tickers,file)

