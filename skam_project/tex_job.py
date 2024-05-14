import telebot
from telebot import types

bot = telebot.TeleBot('6929101322:AAGXbxh9kCuFP08KepObXxEyj3PBwe4sNms')




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'В боте ведутся технические работы')


@bot.message_handler(content_types=['text'])
def tex(message):
    if message.text != 123:
        bot.send_message(message.chat.id, 'В боте ведутся технические работы')





bot.polling()