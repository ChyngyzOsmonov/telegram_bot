import requests
from bs4 import BeautifulSoup

url = 'https://valuta.kg/'

def get_html(url):
    r = requests.get(url) 
    return r.text
        
html = get_html(url)

def get_buy_usd(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find('td').find('a').get('href')
    return ads

def get_sell_usd(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find('td').find_next('td').find('a').get('href')
    return ads

def get_buy_euro(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find_next('tr').find('td').find('a').get('href')
    return ads

def get_sell_euro(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find_next('tr').find('td').find_next('td').find('a').get('href')
    return ads

def get_buy_rub(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find_next('tr').find_next('tr').find('td').find('a').get('href')
    return ads

def get_sell_rub(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find_next('tr').find_next('tr').find('td').find_next('td').find('a').get('href')
    return ads

def get_buy_tenge(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find_next('tr').find_next('tr').find_next('tr').find('td').find('a').get('href')
    return ads

def get_sell_tenge(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='kurs-bar__item').find('table', class_='kurs-table').find_next('table', class_='kurs-table').find_next('table', class_='kurs-table').find('tbody').find('tr').find_next('tr').find_next('tr').find_next('tr').find('td').find_next('td').find('a').get('href')
    return ads





