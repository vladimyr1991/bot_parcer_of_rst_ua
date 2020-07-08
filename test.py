import random

import telebot
from telebot.types import Message

TOKEN = '1315762320:AAGrFbOXp4w427CeGY_ofPxCyCR5-Uu5gf0'
STICKER = 'CAACAgIAAxkBAAMWXvzXF0uv5uC6PiR6baq00_jS7L8AAk4AA7aPSgnHCXNG_QI0jBoE'
USERS = set()
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Привет это всп функции!')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if message.from_user.id in USERS:
        bot.reply_to(message, f'{message.from_user.first_name} снова привет!')
    else:
        bot.reply_to(message, 'Получилось)')
        USERS.add(message.from_user.id)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message:Message):
    bot.send_sticker(message.chat.id, STICKER)
    bot.send_message(message.chat.id, 'Лови еще один')

bot.polling(timeout=60)