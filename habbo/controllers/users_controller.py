# Módulos do G-Earth
from g_python.htools import Direction
from g_python.htools import HMessage

# Variáveis de controle
from controllers.auxiliar.control_data import users_in_room, room_total_mods, mods_in_room, curren_room_id, on_attack_flag, get_attack_flag

# Módulos auxiliares
from controllers.auxiliar.log_functions import log_entry, log_leave, log_error
from controllers.attack_controller import handle_attack_entry




# HANDLE USER ENTRY
def on_users_packet(message : HMessage):
    try:
        packet = message.packet
        # Número de usuários no pacote recebido (user_count == 1: novo usuário entrou no quarto) (user_count > 1: a conta entrou no quarto e o pacote contém os usuários já presentes.)
        user_count = packet.read_int() 

        if user_count == 1:
            (user_unique_id, user_nickname, s, s, user_room_index, i, i, s, i, i, s, i, i, i, i, b) = packet.read("isssiiisiisiiiib")
            
            user_info = {
                'unique_id': user_unique_id,
                'nickname': user_nickname,
                'index': user_room_index
            }

            users_in_room.append(user_info)

            # Confere se o usuário é portador e realiza o log de acordo.
            if user_is_mod(user_nickname):
                mods_in_room.append(user_info)
                try:
                    log_entry(user_nickname, is_mod=True)
                    if get_attack_flag():
                        handle_attack_entry('entrou', user_nickname)
                except Exception as err:
                    log_error("FALHA AO REALIZAR LOG DE ENTRADA DE PORTADOR")
            else:
                try:
                    log_entry(user_nickname)
                except Exception as err:
                    log_error("FALHA AO REALIZAR LOG DE ENTRADA DE USUARIO")          
            return
        
        for _ in range(user_count):
            (user_unique_id, user_nickname, s, s, user_room_index, i, i, s, i, i, s, i, i, i, i, b) = packet.read("isssiiisiisiiiib")
        
            user_info = {
                'unique_id': user_unique_id,
                'nickname': user_nickname,
                'index': user_room_index
            }

            users_in_room.append(user_info)

            if user_is_mod(user_nickname):
                mods_in_room.append(user_info)
                try:
                    log_entry(user_nickname, is_mod=True)
                except Exception as err:
                    log_error("FALHA AO REALIZAR LOG DE ENTRADA DE PORTADOR")

    except Exception as err: # Caso ocorra um erro no recebimento do pacote, podendo ocasionar problemas maiores para a execução do sistema como um todo.
        ... # Realizar envio de mensagem de aviso via Telegram - Pendente


# HANDLE USER LEAVE
def on_user_remove(user):
    temp = str(user).split(": ")

    if len(temp) == 2:
        user_room_index = temp[0]
        user_nickname = temp[1].split(" - ")[0]

        if user_is_mod(user_nickname):
            log_leave(user_nickname, is_mod=True)
            if get_attack_flag():
                handle_attack_entry('saiu', user_nickname)
        else:
            log_leave(user_nickname)

def user_is_mod(user_nickname):
    return user_nickname in room_total_mods


