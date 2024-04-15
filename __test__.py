from telegram_collector.__main__ import *

if __name__ == '__main__':
    collector = new_telegram_collector()
    collector.send_new_message_src_to_dest()