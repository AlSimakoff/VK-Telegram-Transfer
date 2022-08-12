from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events, types
import to_vk

API_ID = '14260225'
API_HASH = '587676597964ac0bbf1fc20a243877be'
SESSION_STRING = '1ApWapzMBu0uLaL7_8_SDe4tAKec3Hla-ZDv400c1lwomczr5ePcaB0FXX6DE7NkXc-Zmd8NwL_97v9c8p54nB3MGnr668bpx5G1pLP-GRsZhKbDNk5-49a0ZCo5WTPsFSMO5TrqnOCuoLk-w70UOGDft322vhYxp9eZYQHcl9SwTP6YSz7lt6lTOfrTWR0QV3ovMY2QOB2hesQAHl1mbOww-YOGgBeS6B3GI53rrjjJvsx6nP0pMZ5oUK1Z6g2Ye2SnG6O7bJufkdDZjCwHEROI3LzXBeFg3SKZVBUxydmO1O-JGbFHs_PL8bAQ0Sf_10g9AIIXZPogiNdEw4qsCQjHCl9Ky68Y='


client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
client.start()
me=client.get_me()
chat=types.PeerChannel(1714740849)
@client.on(events.NewMessage(chat))
async def normal_handler(event):
    if event.message.sender_id!=me.id:
        to_vk.write_msg(event.message.message)

client.run_until_disconnected()