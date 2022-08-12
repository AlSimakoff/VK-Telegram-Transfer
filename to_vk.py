import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkApi
from vk_api.utils import get_random_id
import json, random


API_VERSION = "5.131"
GROUP_ID = "164315210"
GROUP_TOKEN = "vk1.a.IY2abUF4QT-hc3aBXntG1idd-kB2c_SCPOOmwTZA5Xd6NaRDt-V2m8tWQQMKb5VuPRV9WkHoj2PjE7VnIIScZQ52l5QeSauHmqNtKFbe4T1QmfQHA05qyJfgI2pdY9dBycHc3b9RJdPtYuH_sT8eENnRPbEVEZm_g5-1A4xI2RgT9k4vF34xfDCrF61NKpHi"
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()
peer_id = "2000000003"



def write_msg(message):
    
    attachment = ""
    if message == "":
        message 
    
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'attachment': attachment,'random_id': random.getrandbits(64)})
