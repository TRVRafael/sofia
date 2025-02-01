def register_message(user_nickname, text, timestamp, room_messages_list : list):
    try:
        with open(r"sofia\habbo\controllers\listeners\files\messages.txt", "a") as file:
            file.write(f"[{timestamp}] {user_nickname}: {text}")

    except Exception as err:
        print(err)

