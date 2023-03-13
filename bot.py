import telebot
import requests
import os

from dotenv import load_dotenv
from telebot.types import Message

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOTTOKEN'))


@bot.message_handler(commands=['start'])
def hello_message(message: Message):
    text = f'Привет {message.from_user.username}! 👋\n'\
           f'Этот бот показывает погоду в городах по всему миру 🌤️\n' \
           f'Чтобы узнать погоду в интересующем тебя городе, просто введи его название 🔎'

    bot.send_message(chat_id=message.chat.id, text=text)


# дальше бот слушает любое вводимое сообщение (по идее это название города)
@bot.message_handler()
def hello(message):
    # город который ввел пользователь
    input_town = message.text

    payload = {'access_key': os.getenv('APIKEY'), 'query': {input_town}}
    info = requests.get('http://api.weatherstack.com/current', params=payload).json()

    try:
        town = info['location']['name']
        cuuntry = info['location']['country']
        localtime = info['location']['localtime'].split()[-1]
        temp = info['current']['temperature']
        feelslike = info['current']['feelslike']
        wind_speed = info['current']['wind_speed']

        text = f'Страна: {cuuntry}\n' \
               f'Город: {town}\n' \
               f'Местное время: {localtime}\n' \
               f'Температура: {temp}\n' \
               f'Oщущается как: {feelslike}\n' \
               f'Скорость ветра: {wind_speed}м/с'

    except:
        text = f'К сожалению, такого города не найдено ☹️\n' \
               f'Пожалуйста, проверьте правильность написания' \

    bot.send_message(chat_id=message.chat.id, text=text)






bot.infinity_polling()

