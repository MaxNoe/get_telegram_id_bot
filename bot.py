import telepot
import os
from time import sleep


def send_id(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    user_id = msg['from']['id']
    name = msg['from'].get('first_name', '') + ' ' + msg['from'].get('last_name', '')

    if content_type == 'text':
        bot.sendMessage(
            chat_id,
            'Hello {}! Your telegram id is: {}'.format(name, user_id)
        )


bot = telepot.Bot(os.environ['BOT_TOKEN'])
bot.message_loop(send_id)

while True:
    sleep(10)
