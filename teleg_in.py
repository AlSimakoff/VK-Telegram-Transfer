''' Send message from vk'''
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient



def prinyalotvk(id, message):
    API_ID = '***'
    API_HASH = '***'
    SESSION_STRING = '***'

    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    client.start()
    chat=client.get_entity('@Kecsik')
    message= f'{id}:\n{message}'
    client.send_message(chat,message)


