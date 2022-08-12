from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events
import to_vk

API_ID = '14260225'
API_HASH = '587676597964ac0bbf1fc20a243877be'
SESSION_STRING = '1ApWapzMBu2jQgNL6zw-yll70DuiSyVEq-0HvTXObRIKQmmTHnfF-ZoGIEEmY0luWAv-5WhIPtApKiMus6-dxNR59yDcN4h2X249RnMrDWG0bhAb6_8dVNtqBwiI33D_8v-7fX7sAe6oOf5hZ22vHkWyTh2eS82JGC25VM44N7pgazgsR5uyAZIPKvHDKHhYNxNf0hAje0qHBjykZdSXwXHv_JXIqYCbh-dLkWLPwz_5_EPyJ0kjqfc3Yq3W4BuD658RtNEEqK4jo0fq_hN2LGBx2w_1CoFH-e1Xgjmm-jBgUlZML37K7E294Ps4iQ6IHfrfjIyggBtFPXtzww_s2uFklQMefOoY='

#id, message=prinyalotvk()

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
client.start()

@client.on(events.NewMessage)
async def normal_handler(event):
    pass
    to_vk.write_msg(event.message)