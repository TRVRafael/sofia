from telebot import TeleBot

from config.chats_id import CHAT_ID

from handlers.auxiliar.timestamp import get_timestamp


def send_attack_sign_handler(bot : TeleBot, portador, mods_list):
    bot.send_message(CHAT_ID, f"<b>Ataque em base reportado!</b> \n\nComando ativado por: <b>{portador}</b>", message_thread_id=758, parse_mode="HTML")
    bot.send_message(CHAT_ID, "Inicilizando todos procedimentos de segurança pré-definidos.", message_thread_id=2)
    bot.send_message(CHAT_ID, f"-- <b>PORTADORES EM BASE NO MOMENTO</b> --\n\n{handle_mods_list(mods_list)}", message_thread_id=2, parse_mode="HTML")
    

def handle_mods_list(mods_list):
    nick_list = "\n".join([item["nickname"] for item in mods_list])
    return nick_list


def send_doorway_sign_handler(bot: TeleBot, status, nickname):
    bot.send_message(CHAT_ID, f"{nickname} {status} em base - <i>{get_timestamp()}</i>", message_thread_id=2, parse_mode="HTML")
