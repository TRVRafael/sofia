import sqlite3

# def register_message(user_nickname, text, timestamp, room_messages_list : list):
#     try:
#         with open(r"habbo\controllers\listeners\files\messages.txt", "a") as file:
#             file.write(f"[{timestamp}] {user_nickname}: {text}")

#     except Exception as err:
#         print(err)


# Conectar ao banco de dados (ou criar se não existir)
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Criar a tabela de mensagens (se não existir)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT,
            message TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()