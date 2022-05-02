#Файл в котором будет находится основной исполняемый код бота

import telebot
from Setting import ApiKeyTelegramBot
from Markup import markupStart
from Markup import markupScreen
from Markup import markupMessage
from String import *

bot = telebot.TeleBot(ApiKeyTelegramBot)

#-Отправка стартового сообщения-------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, MessageStart, reply_markup=markupStart)


#-Обработка текстовых комманд---------------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def textByUser(msg):
    if msg.chat.type == 'private':
        if msg.text == 'Меню':
            bot.send_message(msg.chat.id, MessageScreen1, reply_markup=markupScreen)
        elif msg.text == 'Давай начнём работу.':
            bot.send_message(msg.chat.id, MessageStartActive, reply_markup=markupScreen)
        elif msg.text == 'Постой, я не готов.':
            bot.send_message(msg.chat.id, MessageStop, reply_markup=markupStart)
        elif msg.text == 'Помощь и краткая аннотация к боту.':
            bot.send_message(msg.chat.id, MessageHelp, reply_markup=markupStart)
        elif msg.text == 'Создание онлайн-визитки':
            bot.send_message(msg.chat.id, MessageStartCreate, reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(msg.chat.id, MessageCreatingCard, reply_markup=markupMessage)

        else:
            bot.send_message(msg.chat.id, MessageError, reply_markup=markupStart)


#-Обработка экранных кнопок-----------------------------------------------------------------------------------------------------------


bot.polling(none_stop = True)
