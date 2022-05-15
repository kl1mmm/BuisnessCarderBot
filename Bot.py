#Файл в котором будет находится основной исполняемый код бота

import telebot
from Setting import ApiKeyTelegramBot
from Markup import markupStart
from Markup import markupScreen
from Markup import markupMessage
from Markup import markupAddContacts
from String import *

bot = telebot.TeleBot(ApiKeyTelegramBot)

DataClient = []

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

@bot.message_handler(content_types=['text'])
def after_text_Discrip(msg):
    DataClient[0] = msg.Text
def after_text_Phone(msg):
    DataClient[1] = msg.Text
def after_text_Email(msg):
    DataClient[2] = msg.Text
def after_text_Address(msg):
    DataClient[3] = msg.Text


#-Обработка экранных кнопок-----------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: c.data)
def card_handling(callback):
    DiscripAdd, ContactsAdd = False, False
    if callback.data == 'discription':
        bot.send_message(chat_id=callback.message.chat.id, text=MessageAskDiscrip)
        bot.send_message(chat_id=callback.message.chat.id, text=MessageDiscripExample)


        bot.answer_callback_query(callback.id, text="Отлично. Теперь описание реализовано.")
        DiscripAdd = True
    if callback.data == 'contacts':
        Phone, Email, Address = False, False, False
        bot.send_message(chat_id=callback.message.chat.id, text=MessageAskContacts, reply_markup=markupAddContacts)
        if callback.data == 'phone':
            msg = bot.send_message(chat_id=callback.message.chat.id, text='Отправь нужный номер телефона')
            bot.register_next_step_handler(msg, after_text_Phone)
            bot.answer_callback_query(callback.id, text="Номер телефона получен.")
            Phone = True
        if callback.data == 'email':
            Email = True
        if callback.data == 'address':
            Address = True

        bot.answer_callback_query(callback.id, text="Контакты были внесены в визитку.")
        ContactsAdd = True


bot.polling(none_stop = True)

