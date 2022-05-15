#Файл в котором будет находится клавиатура и кнопки используемы ботом
from telebot import types

#-Кнопки-----------------------------------------------------------------------------------------------------------------------
StartKey = types.KeyboardButton(text='Давай начнём работу.')
KeyHelp = types.KeyboardButton(text='Помощь и краткая аннотация к боту.')

KeyScreen = types.KeyboardButton('Меню')

KeyGo = types.KeyboardButton('Создание онлайн-визитки')
KeyStop = types.KeyboardButton('Постой, я не готов.')

###KeyAddPhoto = types.InlineKeyboardButton('Фото', callback_data='photo') --- В логистической реализации
KeyAddDiscrip = types.InlineKeyboardButton('Подпись', callback_data='discription')
KeyAddContacts = types.InlineKeyboardButton('Контакты', callback_data='contacts')

KeyContactsPhone = types.InlineKeyboardButton('Телефон', callback_data='phone')
KeyContactsEmail = types.InlineKeyboardButton('Эл. почта', callback_data='email')
KeyContactsAddress = types.InlineKeyboardButton('Адрес', callback_data='address')


#-Меню старта------------------------------------------------------------------------------------------------------------------
markupStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupStart.add(StartKey, KeyHelp)


#-Меню на экране---------------------------------------------------------------------------------------------------------------
markupScreen = types.ReplyKeyboardMarkup()
markupScreen.add(KeyGo, KeyStop)


#-Меню в сообщении-------------------------------------------------------------------------------------------------------------
markupMessage = types.InlineKeyboardMarkup()
markupMessage.add(KeyAddDiscrip, KeyAddContacts)


markupAddContacts = types.InlineKeyboardMarkup()
markupAddContacts.add(KeyContactsPhone, KeyContactsEmail, KeyContactsAddress)
