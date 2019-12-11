import requests
from bs4 import BeautifulSoup
from links_valuta import *

url = get_sell_rub(html)

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

def get_number(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        number = soup.find('div', class_='content-wrap').find('table', class_='vl-list table -no-pad-top -border-last -no-cursor').find('tbody').find('tr').find('td').find_next('td').find_next('td').find_next('td').text
        return number
    except:
        number = ''


def get_location(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        location = soup.find('div', class_='content-wrap').find('table', class_='vl-list table -no-pad-top -border-last -no-cursor').find('tbody').find('tr').find('td').find_next('td').find_next('td').find_next('td').find_next('td').text
        return location
    except:
        location = ''

sell_rub = get_price_rub(html)
sell_ru_title = get_title_rub(html)
sell_ru_number = get_number(html)
sell_ru_location = get_location(html)