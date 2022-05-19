#Файл в котором будет находится основной исполняемый код бота

import telebot
from PIL import Image, ImageDraw, ImageFont
from Setting import ApiKeyTelegramBot
from Markup import markupStart
from Markup import markupScreen
from Markup import markupMessage
from Markup import markupAddContacts
from Markup import markupFinalLoad
from Markup import markupSelectTemplate
from Markup import markupThanks
from Markup import markupGetCard
from Markup import markupRemove
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
        elif msg.text == 'Создать визитку.':
            bot.send_message(msg.chat.id, MessageStartActive, reply_markup=markupScreen)
        elif msg.text == 'Стоп. Я не готов.':
            bot.send_message(msg.chat.id, MessageStop, reply_markup=markupStart)
        elif msg.text == 'Помощь и краткая аннотация к боту.':
            bot.send_message(msg.chat.id, MessageHelp, reply_markup=markupStart)
        elif msg.text == 'Создание.':
            bot.send_message(msg.chat.id, MessageStartCreate, reply_markup=telebot.types.ReplyKeyboardRemove())
            bot.send_message(msg.chat.id, MessageCreatingCard, reply_markup=markupMessage)
        elif msg.text == 'Завершить создание визитки 📌.':
            bot.send_message(msg.chat.id, 'Выбери шаблон визитки:')
            var1example = open('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/var1-example.png', 'rb')
            var2example = open('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/var2-example.png', 'rb')
            var3example = open('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/var3-example.png', 'rb')
            bot.send_photo(msg.chat.id, var1example, caption='Вариант №1️⃣')
            bot.send_photo(msg.chat.id, var2example, caption='Вариант №2️⃣')
            bot.send_photo(msg.chat.id, var3example, caption='Вариант №3️⃣')
            message_to_next_step = bot.send_message(msg.chat.id, MessageSelectTemplate, reply_markup=markupSelectTemplate)
            bot.register_next_step_handler(message_to_next_step, SelectTemplate)
        elif msg.text == 'Получить визитку.':
            visit_card = open('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/BuisnessCard.png', 'rb')
            bot.send_document(msg.chat.id, visit_card, reply_markup=markupThanks)
        elif msg.text == 'Благодарю!':
            bot.send_message(chat_id=msg.chat.id, text='Рад быть полезным.', reply_markup=markupRemove)
            bot.send_message(chat_id=msg.chat.id, text='При желании создать новую визитку, пиши: "Меню" ⚙️.')
        else:
            bot.send_message(msg.chat.id, MessageError, reply_markup=markupStart)


@bot.message_handler(content_types=['text'])
def SelectTemplate(msg):
    if msg.text == 'Первый вариант':
        bot.send_message(chat_id=msg.chat.id, text='Нажми на кнопку через 5 секунд, чтобы получить свою визитку.',
                         reply_markup=markupGetCard)
        img = '/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/template1.png'
        bot.send_message(chat_id=msg.chat.id, text='Генерация визитки 🔄...')
        creating_visit_Card1(img)
    elif msg.text == 'Второй вариант':
        bot.send_message(chat_id=msg.chat.id, text='Нажми на кнопку через 5 секунд, чтобы получить свою визитку.',
                         reply_markup=markupGetCard)
        img = '/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/template2.png'
        bot.send_message(chat_id=msg.chat.id, text='Генерация визитки 🔄...')
        creating_visit_Card2(img)
    elif msg.text == 'Третий вариант':
        bot.send_message(chat_id=msg.chat.id, text='Нажми на кнопку через 5 секунд, чтобы получить свою визитку.',
                         reply_markup=markupGetCard)
        img = '/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/template3.png'
        bot.send_message(chat_id=msg.chat.id, text='Генерация визитки 🔄...')
        creating_visit_Card3(img)


@bot.message_handler(content_types=['text'])
def after_text_Name(msg):
    DataClient[0] = msg.text
    msg = bot.send_message(chat_id=msg.chat.id, text='Специализация:')
    bot.register_next_step_handler(msg, after_text_Spec)
def after_text_Spec(msg):
    DataClient[1] = msg.text
    global DiscripAdd
    DiscripAdd = True
    if ContactsAdd == False:
        bot.send_message(chat_id=msg.chat.id, text='Карткая информация внесена. Далее выбери раздел "Контакты" в сообщении выше.')
    else:
        bot.send_message(chat_id=msg.chat.id, text='Данные для визитки готовы.', reply_markup=markupFinalLoad)
    exit()
def after_text_Phone(msg):
    DataClient[2] = msg.text
    global Phone
    Phone = True
    bot.send_message(chat_id=msg.chat.id, text="Номер телефона - ✅")
    bot.send_message(chat_id=msg.chat.id, text=MessageFinalLoad, reply_markup=markupFinalLoad)
def after_text_Email(msg):
    DataClient[3] = msg.text
    global Email
    Email = True
    bot.send_message(chat_id=msg.chat.id, text='Почта - ✅')
def after_text_Address(msg):
    DataClient[4] = msg.text
    global Address
    Address = True
    bot.send_message(chat_id=msg.chat.id, text='Адрес - ✅')


#-Обработка экранных кнопок-----------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda c: c.data)
def card_handling(callback):
    if callback.data == 'discription':
        bot.send_message(chat_id=callback.message.chat.id, text=MessageAskDiscrip)
        msg = bot.send_message(chat_id=callback.message.chat.id, text=MessageDiscripExample)
        bot.register_next_step_handler(msg, after_text_Name)

    if callback.data == 'contacts':
        bot.answer_callback_query(callback.id, text="Описание реализовано ✅.")
        bot.send_message(chat_id=callback.message.chat.id, text=MessageAskContacts, reply_markup=markupAddContacts)
    if callback.data == 'phone':
        msg = bot.send_message(chat_id=callback.message.chat.id, text='Номер телефона: ')
        bot.register_next_step_handler(msg, after_text_Phone)
    if callback.data == 'email':
        msg = bot.send_message(chat_id=callback.message.chat.id, text='Электронная почта: ')
        bot.register_next_step_handler(msg, after_text_Email)
    if callback.data == 'address':
        msg = bot.send_message(chat_id=callback.message.chat.id, text='Указываемый адрес: ')
        bot.register_next_step_handler(msg, after_text_Address)


def creating_visit_Card1(img):
    Template = Image.open(img)
    MainFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/ofont.ru_Bebas Neue.ttf', size=54)
    SecFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/BebasNeue-Light.otf', size=34)
    ThirdFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/montserrat-light.ttf', size=20)
    TempDraw = ImageDraw.Draw(Template)
    TempDraw.text((150, 140), DataClient[0], font=MainFont, fill='black')
    TempDraw.text((150, 230), DataClient[1], font=SecFont, fill='black')
    TempDraw.text((790, 370), DataClient[2], font=ThirdFont, fill='black')
    TempDraw.text((740, 400), DataClient[3], font=ThirdFont, fill='black')
    TempDraw.text((530, 430), DataClient[4], font=ThirdFont, fill='black')
    Template.save('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/BuisnessCard.png')

def creating_visit_Card2(img):
    Template = Image.open(img)
    MainFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/CATNeuzeit.ttf', size=54)
    SecFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/ofont.ru_Clear Sans.ttf', size=23)
    ThirdFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/ofont.ru_Clear Sans.ttf', size=27)
    TempDraw = ImageDraw.Draw(Template)
    TempDraw.text((42, 130), DataClient[0], font=MainFont, fill='black')
    TempDraw.text((46, 210), DataClient[1], font=SecFont, fill='black')
    TempDraw.text((350, 335), 'Мобильный телефон: '+DataClient[2], font=ThirdFont, fill='black')
    TempDraw.text((350, 370), 'Эл.почта: '+DataClient[3], font=ThirdFont, fill='black')
    TempDraw.text((350, 405), 'Адрес: '+DataClient[4], font=ThirdFont, fill='black')
    Template.save('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/BuisnessCard.png')

def creating_visit_Card3(img):
    Template = Image.open(img)
    MainFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/crimson_roman.otf', size=54)
    SecFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/SourceSansPro-Light.ttf', size=23)
    ThirdFont = ImageFont.truetype('/Users/ilyaklimov/Library/Fonts/SourceSansPro-Light.ttf', size=27)
    TempDraw = ImageDraw.Draw(Template)
    TempDraw.text((505, 60), DataClient[0], font=MainFont, fill='#3a4520')
    TempDraw.text((510, 215), DataClient[1], font=SecFont, fill='#975c10')
    TempDraw.text((510, 380), DataClient[2], font=ThirdFont, fill='#3a4520')
    TempDraw.text((510, 410), DataClient[3], font=ThirdFont, fill='#3a4520')
    TempDraw.text((510, 440), DataClient[4], font=ThirdFont, fill='#3a4520')
    Template.save('/Users/ilyaklimov/Desktop/Учёба/Программная инженерия/BuisenssCarderBot/templates/BuisnessCard.png')

bot.polling(none_stop = True)

