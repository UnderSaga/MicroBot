import telebot
from telebot import types

bot = telebot.TeleBot("8002325739:AAGeU3IRe9CKdoHiok9aH0KtnU_aYkTd2lQ", parse_mode=None)

rules = """
Приветствуем тебя в нашей таверне! Заходи располагайся. 
Дабы всём тут было комфортно, соблюдай некоторые правила! 
1. Вся ругань в личные сообщения. 
2. Реклама без согласования со мной запрещена. 
3. Обсуждение религии и политики запрещено. 
Веди себя хорошо!)
"""

@bot.message_handler(content_types=['new_chat_members'])  
def greeting(message):  
    bot.reply_to(message, text=rules)

@bot.message_handler(func=lambda message: True)
def inviteButton(message):
    if(message.is_automatic_forward):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Присоединиться к Совёнку', url='https://t.me/+kuf7BiVM1Xc1YTdi')
        markup.add(btn1)
        bot.reply_to(message, "Садись за барную стойку! У Совёнка есть пару историй для тебя!", reply_markup = markup)


bot.infinity_polling()