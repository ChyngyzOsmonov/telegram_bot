import requests
from bs4 import BeautifulSoup
from links_valuta import *

url = get_buy_usd(html)

def get_html(url):
    r = requests.get(url) 
    return r.text
        
html = get_html(url)

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


buy_us_number = get_number(html)
buy_us_location = get_location(html)
