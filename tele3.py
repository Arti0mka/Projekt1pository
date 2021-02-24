import os
import sys
import subprocess
import telebot
import time
#pip3 install pytelegrambotapi --upgrade

bot = telebot.TeleBot('1287725214:AAEPpUk4MmCQOl5FDBs5IiF3zzNRQXHnB6Q')
arin = 0
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global arin
    if str(message.from_user.id) == "1226994201":
       arin = arin + 1
    if str(message.from_user.id) == "1369930501":
       arin = arin + 5
    print(message.text)
    if message.text == "/help":
        bot.send_message(message.from_user.id, "i am stupit")        
    print(message.text)
    if message.text == "Мими":
        bot.send_message(message.from_user.id, "user.id")
        print(message.text)
        bot.send_message(message.from_user.id, str(message.from_user.id))
    else:
        bot.send_message(message.from_user.id, arin)

bot.polling(none_stop=True, interval=0)
