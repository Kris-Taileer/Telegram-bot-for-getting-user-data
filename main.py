import userdata
from userdata import telebot
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

from telebot import types

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("hi?")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "hi there man, nice to meet u", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'hi?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton('url')
        #btn2 = types.KeyboardButton('Правила сайта')
        #btn3 = types.KeyboardButton('Советы по оформлению публикации')
        #markup.add(btn1)
        bot.send_message(message.from_user.id, 'i have something nice for u, use <url>', reply_markup=markup)
        btn2 = types.KeyboardButton("url")
        markup.add(btn2)
        @bot.message_handler(commands = ['url'])
        def url(message):
            markup = types.InlineKeyboardMarkup()
            btn3 = types.InlineKeyboardButton(text="portal to Nedoserver's world", url='https://mc.marduk.ru')
            markup.add(btn3)
            bot.send_message(message.from_user.id, "click right here!", reply_markup = markup)
            bot.send_message(message.from_user.id, 'if u want to see more about author of Nedoerver, look right ' + '[here](http://marduk.ru)', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)