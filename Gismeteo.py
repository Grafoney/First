import requests
from bs4 import BeautifulSoup

url = "https://www.gismeteo.ru/"


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    r = requests.get(url, headers=headers)
    return r.text
def parse(html):
    soup = BeautifulSoup(html)
    h2 = soup.find("h2", class_ = "typeC")
    print (h2.prettify())
    dd = soup.find("dd",class_ = "value m_temp c")
    print (dd.prettify())

def main():
    parse(get_html(url))

print(main())
