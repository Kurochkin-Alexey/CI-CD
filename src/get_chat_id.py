import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(token=BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def print_chat_id(message):
    print(message.from_user.id)

bot.infinity_polling()
