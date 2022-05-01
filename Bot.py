#Файл в котором будет находится основной исполняемый код бота

import telebot
from Setting import ApiKeyTelegramBot
from Markup import markupStart
from Markup import markupScreen
from String import MessageStart
from String import MessageStartActive
from String import MessageScreen1
from String import MessageError
from String import MessageTest

bot = telebot.TeleBot(ApiKeyTelegramBot)

#-Отправка стартового сообщения-------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, MessageStart, reply_markup=markupStart)


#-Обработка текстовых комманд---------------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def textByUser(msg):
    if msg.chat.type == 'private':
        if msg.text == 'Экранные кнопки':
            bot.send_message(msg.chat.id, MessageScreen1, reply_markup=markupScreen)
        elif msg.text == 'Начать создание визитки':
            bot.send_message(msg.chat.id, MessageStartActive, reply_markup=markupScreen)
        elif msg.text == 'Кнопка 1' or msg.text == 'Кнопка 2':
            pass
        else:
            bot.send_message(msg.chat.id, MessageError, reply_markup=markupStart)


#-Обработка экранных кнопок-----------------------------------------------------------------------------------------------------------


bot.polling(none_stop = True)
