#Файл в котором будет находится основной исполняемый код бота

import telebot
from Setting import ApiKeyTelegramBot
from Markup import markupStart
from String import MessageStart

bot = telebot.TeleBot(ApiKeyTelegramBot)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, MessageStart, reply_markup=markupStart)

def main():
    bot.polling(none_stop=True)
if __name__ == '__main__':
    main()