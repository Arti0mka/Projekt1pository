import os
import sys
import subprocess
import telebot
import time
from telebot import types
import ast
#pip3 install pytelegrambotapi --upgrade

oButtonConfig = {"one": "key_one", "two": "key_two", "three": "key_three"}
oButtonConfig = {"four": "key_four", "five": "key_five", "six": "key_six"}
oButtonConfig = {"seven": "key_seven", "eight": "key_eight", "nine": "key_nine"}
def makeKeyboard(oArr):
        markup = types.InlineKeyboardMarkup()
        a1 = types.InlineKeyboardButton(text="1",callback_data="key_1")
        a2 = types.InlineKeyboardButton(text="2",callback_data="key_2")
        a3 = types.InlineKeyboardButton(text="3",callback_data="key_3")
        a4 = types.InlineKeyboardButton(text="4",callback_data="key_4")
        a5 = types.InlineKeyboardButton(text="5",callback_data="key_5")    
        a6 = types.InlineKeyboardButton(text="6",callback_data="key_6") 
        a7 = types.InlineKeyboardButton(text="7",callback_data="key_7")    
        a8 = types.InlineKeyboardButton(text="8",callback_data="key_8")    
        a9 = types.InlineKeyboardButton(text="9",callback_data="key_9")    
        markup.add(a1,a2,a3)
        markup.add(a4,a5,a6)
        markup.add(a7,a8,a9)
        return markup
        for value,key in oArr.items():
         markup.add(types.InlineKeyboardButton(text=value,      
                 callback_data="['value', '" + value + "', '" + key + "']"))
        return markup

bot = telebot.TeleBot('1287725214:AAEPpUk4MmCQOl5FDBs5IiF3zzNRQXHnB6Q')


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    print(call.data)
    if call.data.startswith("key_1") :
        bot.send_message(chat_id=call.message.chat.id,text="you send one button")
    elif call.data.startswith("key_2") :
        bot.send_message(chat_id=call.message.chat.id,text="you send two button")
    elif call.data.startswith("key_3") :
        bot.send_message(chat_id=call.message.chat.id,text="you send three button")
    elif call.data.startswith("key_4") :
        bot.send_message(chat_id=call.message.chat.id,text="you send four button")
    elif call.data.startswith("key_5") :
        bot.send_message(chat_id=call.message.chat.id,text="you send five button")
    elif call.data.startswith("key_6") :
        bot.send_message(chat_id=call.message.chat.id,text="you send six button")
    elif call.data.startswith("key_7") :
        bot.send_message(chat_id=call.message.chat.id,text="you send seven button")
    elif call.data.startswith("key_8") :
        bot.send_message(chat_id=call.message.chat.id,text="you send eight button")
    elif call.data.startswith("key_9") :
        bot.send_message(chat_id=call.message.chat.id,text="you send nine button")
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
