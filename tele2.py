import os
import sys
import subprocess
import telebot
import time
from telebot import types
import ast
#pip3 install pytelegrambotapi --upgrade

oButtonConfig = {"one": "key_one", "two": "key_two", "three": "key_three"}

def makeKeyboard(oArr):
    markup = types.InlineKeyboardMarkup()
    for value,key in oArr.items():
        markup.add(types.InlineKeyboardButton(text=value,
                 callback_data="['value', '" + value + "', '" + key + "']"))
    return markup

bot = telebot.TeleBot('1287725214:AAEPpUk4MmCQOl5FDBs5IiF3zzNRQXHnB6Q')


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if (call.data.startswith("['value'")):
        valueFromCallBack = ast.literal_eval(call.data)[1]
        messTXT = ast.literal_eval(call.data)[2]
    if messTXT == "key_one":
        bot.send_message(chat_id=call.message.chat.id,text="you send one button")
    elif messTXT == "key_two":
        bot.send_message(chat_id=call.message.chat.id,text="you send two button")
    elif messTXT == "key_three":
        bot.send_message(chat_id=call.message.chat.id,text="you send three button")
    else:
        bot.send_message(chat_id=call.message.chat.id,text="write artem for create new keyboard")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if message.text == "/help":
        bot.send_message(message.from_user.id, "i am stupit")
    elif message.text == "artem":
        bot.send_message(chat_id=message.chat.id,
                text="Here are the general tasks",
                reply_markup=makeKeyboard(oButtonConfig),
                parse_mode='HTML')	
    else:
        bot.send_message(message.from_user.id, "i undestend write /help.")

bot.polling(none_stop=True, interval=0)	
