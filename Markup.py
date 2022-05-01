#Файл в котором будет находится клавиатура и кнопки используемы ботом
from telebot import types

#-Кнопки-----------------------------------------------------------------------------------------------------------------------
StartKey = types.KeyboardButton(text='Начать создание визитки')

KeyScreen = types.KeyboardButton('Экранные кнопки')

Key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='1')
Key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='2')
#-Меню старта------------------------------------------------------------------------------------------------------------------
markupStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupStart.add(StartKey)
#-Меню на экране---------------------------------------------------------------------------------------------------------------
markupScreen = types.ReplyKeyboardMarkup()
markupScreen.add(Key1, Key2)
