import telebot

# Вставь сюда свой токен от BotFather
TOKEN = "7686110975:AAG1prcOYUZAxea_pGAGES0o0j1lB16pK7E"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой первый бот!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Ты написал: " + message.text)

bot.polling()
