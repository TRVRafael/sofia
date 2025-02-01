# Módulo telebot
import telebot

# Handlers
from handlers.requests_handler import *

# Módulos de autorização
from config.auth import BOT_TOKEN, BOT_AUX_TOKEN

bot = telebot.TeleBot(BOT_AUX_TOKEN)

def send_attack_sign(portador, mods_list):
    return send_attack_sign_handler(bot, portador, mods_list)

def send_doorway_sign(status, nickname):
    return send_doorway_sign_handler(bot, status, nickname)

if __name__ == "__main__":
    bot.polling()
