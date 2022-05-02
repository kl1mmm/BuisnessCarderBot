#Файл в котором будет находится клавиатура и кнопки используемы ботом
from telebot import types

#-Кнопки-----------------------------------------------------------------------------------------------------------------------
StartKey = types.KeyboardButton(text='Давай начнём работу.')
KeyHelp = types.KeyboardButton(text='Помощь и краткая аннотация к боту.')

KeyScreen = types.KeyboardButton('Меню')

KeyGo = types.KeyboardButton('Создание онлайн-визитки')
KeyStop = types.KeyboardButton('Постой, я не готов.')

KeyAddPhoto = types.InlineKeyboardButton('Фото', callback_data='photo')
KeyAddDiscrip = types.InlineKeyboardButton('Описание', callback_data='discription')
KeyAddContacts = types.InlineKeyboardButton('Контакты', callback_data='contacts')
#-Меню старта------------------------------------------------------------------------------------------------------------------
markupStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupStart.add(StartKey, KeyHelp)
#-Меню на экране---------------------------------------------------------------------------------------------------------------
markupScreen = types.ReplyKeyboardMarkup()
markupScreen.add(KeyGo, KeyStop)
#-Меню в сообщении-------------------------------------------------------------------------------------------------------------
markupMessage = types.InlineKeyboardMarkup()
markupMessage.add(KeyAddPhoto, KeyAddDiscrip, KeyAddContacts)
