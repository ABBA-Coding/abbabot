from telebot import TeleBot
from telebot.types import Message

from config import *
from keyboards import webbutton

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    for admin in ADMINS:
        bot.send_message(admin, f'Assalomualeykum, {message.from_user.first_name}', reply_markup=webbutton())


if __name__ == '__main__':
    print('Bot ishladi...')
    bot.infinity_polling()