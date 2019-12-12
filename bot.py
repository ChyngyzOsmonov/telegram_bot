import requests
from links_valuta import *
import telebot
from telebot import types
import misc

import buy_best_rub
from buy_best_rub import buy_rub
from buy_best_rub import buy_ru_title
from buy_best_rub import buy_ru_number
from buy_best_rub import buy_ru_location
import sell_best_rub
from sell_best_rub import sell_rub
from sell_best_rub import sell_ru_title
from sell_best_rub import sell_ru_number
from sell_best_rub import sell_ru_location

import buy_best_usd
from buy_best_usd import buy_usd
from buy_best_usd import buy_us_title
from buy_best_usd import buy_us_number
from buy_best_usd import buy_us_location
import sell_best_usd
from sell_best_usd import sell_usd
from sell_best_usd import sell_us_title
from sell_best_usd import sell_us_number
from sell_best_usd import sell_us_location

import buy_best_euro
from buy_best_euro import buy_euro
from buy_best_euro import buy_eu_title
from buy_best_euro import buy_eu_number
from buy_best_euro import buy_eu_location
import sell_best_euro
from sell_best_euro import sell_euro
from sell_best_euro import sell_eu_title
from sell_best_euro import sell_eu_number
from sell_best_euro import sell_eu_location

import buy_best_tenge
from buy_best_tenge import buy_tenge
from buy_best_tenge import buy_kz_title
from buy_best_tenge import buy_kz_number
from buy_best_tenge import buy_kz_location
import sell_best_tenge
from sell_best_tenge import sell_tenge
from sell_best_tenge import sell_kz_title
from sell_best_tenge import sell_kz_number
from sell_best_tenge import sell_kz_location

token = misc.token

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.send_message(
		message.chat.id,
		'''Добро пожаловать. У нас выводится самые лучшие курсы валют по Бишкеку\nПолезные команды для навигации:\nДля выхода в главное меню напишите /end или /start
		''',
		reply_markup = start_keyboard())

@bot.message_handler(content_types=["text"])
def send_anytext(message):    
	chat_id = message.chat.id
	if message.text == 'Покупка':
		bot.send_message(chat_id, 'Вы выбрали раздел покупки', reply_markup = buy_keyboard())
	elif message.text == 'Продажа':
		bot.send_message(chat_id, 'Вы выбрали раздел продаж', reply_markup = sell_keyboard())
	
	elif message.text == 'Покупка 🇷🇺':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(buy_ru_title,buy_rub,buy_ru_number,buy_ru_location))
	elif message.text == 'Продажа 🇷🇺':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(sell_ru_title,sell_rub,sell_ru_number,sell_ru_location))
	
	elif message.text == 'Покупка 🇺🇸':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(buy_us_title,buy_usd,buy_us_number,buy_us_location))
	elif message.text == 'Продажа 🇺🇸':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(sell_us_title,sell_usd,sell_us_number,sell_us_location))

	elif message.text == 'Покупка 🇪🇺':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(buy_eu_title,buy_euro,buy_eu_number,buy_eu_location))
	elif message.text == 'Продажа 🇪🇺':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(sell_eu_title,sell_euro,sell_eu_number,sell_eu_location))

	elif message.text == 'Покупка 🇰🇿':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(buy_kz_title,buy_tenge,buy_kz_number,buy_kz_location))
	elif message.text == 'Продажа 🇰🇿':
		bot.send_message(chat_id, 'Названия банка/обменки: {}\nАктуальный курс: {}\nНомер телефона: {}\nАдрес: {}'.format(sell_kz_title,sell_tenge,sell_kz_number,sell_kz_location))
	elif message.text == '/end':
		bot.send_message(chat_id, 'Вы вышли в главное меню', reply_markup = start_keyboard())
	elif message.text == '🔙':
		bot.send_message(chat_id, 'Вы вышли в главное меню', reply_markup = start_keyboard())

def start_keyboard():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	markup.row('Покупка', 'Продажа')
	return markup  

def buy_keyboard():
	markup1 = types.ReplyKeyboardMarkup(row_width = 2, one_time_keyboard=False, resize_keyboard=True)
	markup1.add('Покупка 🇷🇺',
				'Покупка 🇺🇸',
				'Покупка 🇪🇺', 
				'Покупка 🇰🇿',
				'🔙')
	return markup1  

def sell_keyboard():
	markup = types.ReplyKeyboardMarkup(row_width = 2, one_time_keyboard=False, resize_keyboard=True)
	markup.add('Продажа 🇷🇺',
				'Продажа 🇺🇸',
				'Продажа 🇪🇺',
				'Продажа 🇰🇿',
				'🔙')
	return markup  

if __name__ == "__main__":
	bot.polling(none_stop=True)


