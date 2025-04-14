import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("wbslotfinder_bot")  # Переменная окружения из Render
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я работаю на Render через webhook")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "200 OK", 200

@app.route('/')
def index():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}")
    return "Webhook установлен", 200

if name == "__main__":
    # ВАЖНО: используем порт из Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
