from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient,types



def prinyalotvk(id, message):
    API_ID = '14260225'
    API_HASH = '587676597964ac0bbf1fc20a243877be'
    SESSION_STRING = '1ApWapzMBuxpDfPzF4gpuz29bsX21K22wC-bPUgXIiifZyffGTwRCnb40WRo9ZfPN5nVmXbT8QHfXf89Vrkt3K1BodK6RBAogGwacujwaQHuksSnKiQPvCNc477G--EIhA9cKmjNEgKAD7TjfefyrUiHYuwtIZdViT1AAyXmFphWYstqMKmZGasVbnkhonauIVkiDxoHqECBx09lQQ9UsKLV00ZOTzU7nJRVVLY1YFGGeIeB4NXTnxfQXj4wlBrBuXWyf3DIVHZYxbCGuu_rbDIy1dulJOvCfSU_3W1zhWOqEjhY3s5fUjUnKd152CL89FL775qNTE8phhKiBkAG5xJj-J6YTz24='

    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    client.start()
    chat=types.PeerChannel(1714740849)
    message= f'{id}:\n{message}'
    client.send_message(chat,message)

