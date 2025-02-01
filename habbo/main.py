# Módulos do G-Earth
from g_python.gextension import Extension
from g_python.htools import Direction, RoomUsers

# Controladores
from controllers.users_controller import on_users_packet, on_user_remove
from controllers.messages_controller import on_message

from controllers.attack_controller import check_hide_area

extension_info = {
    "title": 'Torvi. Defense',
    "description": "Sistema de defesa automatizado.",
    "version": "1.0",
    "author": "Torvi."
}

ext = Extension(extension_info, ('-p', '9092'))
ext.start()

room_users = RoomUsers(ext)
room_users.on_remove_user(on_user_remove)

ext.intercept(Direction.TO_CLIENT, on_users_packet, "Users")
ext.intercept(Direction.TO_CLIENT, on_message, "Chat")
ext.intercept(Direction.TO_CLIENT, on_message, "Shout")
ext.intercept(Direction.TO_CLIENT, check_hide_area, "AreaHide")

def exec_hide_area():
    ext.send_to_server('{out:UseFurniture}{b:127}{b:255}{i:0}{s:""}')
