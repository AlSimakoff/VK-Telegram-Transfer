'''Send message from telegram '''
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkApi
from vk_api.utils import get_random_id
import json, random


API_VERSION = "5.131"
GROUP_ID = "***"
GROUP_TOKEN = "***"
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()
peer_id = "2000000003"



def write_msg(message):
    
    attachment = ""
    if message == "":
        message 
    
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'attachment': attachment,'random_id': random.getrandbits(64)})
