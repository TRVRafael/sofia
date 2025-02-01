import logging

# Logging configuration
logging.basicConfig(filename=r'sofia\habbo\controllers\logs\system_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_entry(user_nickname, is_mod = False):
    if is_mod:
        logging.info(f'PORTADOR {user_nickname} ENTROU')
        return
    logging.info(f'USUARIO {user_nickname} ENTROU')


def log_leave(user_nickname, is_mod = False):
    if is_mod:
        logging.info(f'PORTADOR {user_nickname} SAIU')
        return
    logging.info(f'USUARIO {user_nickname} SAIU')


def log_message(user_nickname, message):
    logging.info(f"{user_nickname} FALOU: {message}")


def log_error(message):
    logging.error(message)


def log_attack(message):
    logging.warning(message)
