import requests
from bs4 import BeautifulSoup
from links_valuta import *

url = get_buy_rub(html)

def get_html(url):
    r = requests.get(url) 
    return r.text
        
html = get_html(url)

def get_title_rub(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('table', class_='vl-list table -no-pad-top -border-last -no-cursor').find('tbody').find('tr')
    for ad in ads:
        try:
            name = ad.find('div', class_='td-member__info').find('h4').find('a').text.strip()
            return name
        except:
            name = ''
def get_price_rub(html): 
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('table', class_='vl-list table -no-pad-top -border-last -no-cursor').find('tbody').find('tr') 
    for ad in ads:   
        try:
            buy = ad.find('div', class_='td-rate__wrp').text.strip()
            return buy
        except:
            buy = ''

buy_rub = get_price(html)
buy_ru_title = get_title_rub(html)