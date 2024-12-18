import telebot
from telebot import types
from dotenv import load_dotenv
import os

class Users:
    def __init__(self, id=0, name='', age=0, gender='', balance=0, telegram_id=0):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
        self.telegram_id = telegram_id
