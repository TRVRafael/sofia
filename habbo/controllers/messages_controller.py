# Módulos do G-Earth
from g_python.htools import HMessage

# Variáveis de controle
from controllers.auxiliar.control_data import users_in_room, mods_in_room, set_attack_flag, get_attack_flag, room_messages

# Módulos auxiliares
from controllers.auxiliar.log_functions import log_message, log_attack, log_error
from controllers.listeners.message_listener import register_message
from controllers.auxiliar.auxiliar_functions import get_timestamp

# Módulos adicionais
import requests


def on_message(message : HMessage):
    packet = message.packet
    (user_room_index, text, i, i, i, i) = packet.read("isiiii")

    # Encontrar o usuário na lista users_in_room pelo user_index
    user = next((u for u in users_in_room if u["index"] == user_room_index), None)

    if not user:
        user = {"nickname": "UNKNOWN"}

    if user:
        log_message(user["nickname"], text)  # Registra a mensagem com o nickname
    else:
        log_message(f"Usuário com index {user_room_index} não encontrado. FALOU" , text)

    if "ATK!" in text: # Mensagem recebida no momento do comando: Torvi. ATK!
        set_attack_flag(True)
        activator = text.split(" ")[0]
        log_attack(f"ATAQUE ATIVADO POR {activator}")

        headers = {"Content-Type": "application/json"}
        body = {
            "portador": activator,
            "mods_list": mods_in_room
        }

        try:
            requests.post("http://192.168.0.120:5555/atk_sign", headers=headers, json=body) # Webhook
        except Exception as err:
            log_error(err)


    if not user["nickname"]:
        register_message("DESCONHECIDO", text, get_timestamp(), room_messages)
        return
    if get_attack_flag:
        register_message(user["nickname"], text, get_timestamp(), room_messages)
    