import requests

from g_python.hpacket import HPacket
from g_python.hmessage import Direction, HMessage
from g_python.htools import Extension

def handle_attack_entry(status, user_nickname):
    headers = {"Content-Type": "application/json"}
    body = {
        "status": status,
        "user_nickname": user_nickname
    }

    requests.post("http://192.168.0.120:5555/doorway", headers=headers, json=body)

    

def check_hide_area(message):
    (x, y, s, hide, i, i, i, i, b) = message.packet.read("bbsbiiiib")

    if x == 127 and y == 255 and hide == True: # Hide == True when the area gets hidden, and is false when it gets revealed
        print('yes')

