#Файл в котором будет находится основной исполняемый код бота

import telebot
from Setting import ApiKeyTelegramBot
from Markup import markupStart
from Markup import markupScreen
from Markup import markupMessage
from Markup import markupAddContacts
from Markup import markupFinalLoad
from String import *

bot = telebot.TeleBot(ApiKeyTelegramBot)

DataClient = ['', '', '', '', '']
DiscripAdd, ContactsAdd = False, False
Phone, Email, Address = False, False, False

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
def after_text_Name(msg):
    DataClient[0] = msg.text
    msg = bot.send_message(chat_id=msg.chat.id, text='Специализация:')
    bot.register_next_step_handler(msg, after_text_Spec)


@bot.message_handler(content_types=['text'])
def after_text_Spec(msg):
    DataClient[1] = msg.text
    DiscripAdd = True
    if ContactsAdd == False:
        bot.send_message(chat_id=msg.chat.id, text='Хорошо, краткая информация готова. Теперь, в том же сообщении, где нажимал "Подпись", выбери раздел "Контакты".')
    else:
        bot.send_message(chat_id=msg.chat.id, text='Отлично, данные для визитки полностью внесены!', reply_markup=markupFinalLoad)
    exit()



@bot.message_handler(content_types=['text'])
def after_text_Phone(msg):
    DataClient[2] = msg.text
    Phone = True
    bot.send_message(chat_id=msg.chat.id, text="Номер телефона получен.")
    bot.send_message(chat_id=msg.chat.id, text=MsgFinalLoad, reply_markup=markupFinalLoad)

@bot.message_handler(content_types=['text'])
def after_text_Email(msg):
    DataClient[3] = msg.text
    Email = True
    bot.send_message(chat_id=msg.chat.id, text='Почта успешно записана.')


@bot.message_handler(content_types=['text'])
def after_text_Address(msg):
    DataClient[4] = msg.text
    Address = True
    bot.send_message(chat_id=msg.chat.id, text='Адрес был добавлен!')


#-Обработка экранных кнопок-----------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: c.data)
def card_handling(callback):
    if callback.data == 'discription':
        bot.send_message(chat_id=callback.message.chat.id, text=MessageAskDiscrip)
        msg = bot.send_message(chat_id=callback.message.chat.id, text=MessageDiscripExample)
        bot.register_next_step_handler(msg, after_text_Name)

    if callback.data == 'contacts':
        bot.answer_callback_query(callback.id, text="Отлично. Теперь описание реализовано.")
        bot.send_message(chat_id=callback.message.chat.id, text=MessageAskContacts, reply_markup=markupAddContacts)
    if callback.data == 'phone':
        msg = bot.send_message(chat_id=callback.message.chat.id, text='Отправь нужный номер телефона:')
        bot.register_next_step_handler(msg, after_text_Phone)
    if callback.data == 'email':
        msg = bot.send_message(chat_id=callback.message.chat.id, text='Твоя электронная почта: ')
        bot.register_next_step_handler(msg, after_text_Email)
    if callback.data == 'address':
        msg = bot.send_message(chat_id=callback.message.chat.id, text='Твой адрес для клиентов: ')
        bot.register_next_step_handler(msg, after_text_Address)


bot.polling(none_stop = True)

