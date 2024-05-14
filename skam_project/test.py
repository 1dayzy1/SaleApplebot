import telebot
from datetime import datetime
from telebot import types

TOKEN = '6889712074:AAGhdrxhFE4ZW2Bjoz5msbXuicQZVFWR9fk'
bot = telebot.TeleBot(TOKEN)

start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('btn1')
    btn2 = types.KeyboardButton('btn2')
    btn3 = types.KeyboardButton('My profile')
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id, f'Hi,{message.from_user.username}!',reply_markup=markup)
    start_date
    
@bot.message_handler(content_types=['text'])
def my(message):
    if message.text == 'My profile':
        bot.send_message(message.chat.id, f'data:{start_date}')

bot.polling()