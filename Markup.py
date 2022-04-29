#Файл в котором будет находится клавиатура и кнопки используемы ботом
from telebot import types

StartKey = types.KeyboardButton('Нажми, чтобы начать работу')
markupStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupStart.add(StartKey)