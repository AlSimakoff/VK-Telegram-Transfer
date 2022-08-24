'''pars message from telegram'''
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events
import to_vk

API_ID = '***'
API_HASH = '***'
SESSION_STRING = '***'


client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
client.start()
chat=client.get_entity('@Kecsik')
@client.on(events.NewMessage(chat))
async def normal_handler(event):
    write_msg(event.message.message)

    
client.run_until_disconnected()
