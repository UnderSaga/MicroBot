import telebot
from telebot import types

bot = telebot.TeleBot("8002325739:AAGeU3IRe9CKdoHiok9aH0KtnU_aYkTd2lQ", parse_mode=None)

rules = """
Приветствуем тебя в нашей беседе!
Чтобы продолжить общение, комфортное для всех - ознакомься с правилами:
1. Не пиши;
2. Не дыши;
3. Бан тебе!
"""

@bot.message_handler(content_types=['new_chat_members'])  
def greeting(message):  
    bot.reply_to(message, text=rules)

@bot.message_handler(func=lambda message: True)
def inviteButton(message):
    if(message.is_automatic_forward):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Наша лютая беседка', url='https://t.me/+kuf7BiVM1Xc1YTdi')
        markup.add(btn1)
        bot.reply_to(message, "Садись за барную стойку! У Совёнка есть пару историй для тебя!", reply_markup = markup)


bot.infinity_polling()