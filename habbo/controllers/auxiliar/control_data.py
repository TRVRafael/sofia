# Variáveis de controle 
b1_room_id = 148212967
b2_room_id = ...
hall_room_id = ...


# Variáveis externas
curren_room_id = ''


# Flags internas
on_attack_flag = False
def set_attack_flag(value: bool):
    global on_attack_flag
    on_attack_flag = value


def get_attack_flag():
    global on_attack_flag
    return on_attack_flag


# Listas de controle variáveis de usuário
mods_in_room = [{'unique_id': 80599039, 'nickname': 'rafae9218', 'index': 5}, {'unique_id': 80599039, 'nickname': 'LAV!N', 'index': 3}] # Lista dos portadores presentes no quarto
room_total_mods = ['teste', 'rafae9218', 'oi'] # Lista de todos usuários com direitos no quarto

users_in_room = [] # Lista dos usuários presentes no quarto


# Listas de controle de banimentos
b1_pendent_ban = [] # Lista de usuários com banimento pendente na Base 1
b2_pendent_ban = [] # Lista de usuários com banimento pendente na Base 2

room_banned_users = [] # Lista de usuários banidos do quarto

# Lista de armazenamento de mensagens
room_messages = []

