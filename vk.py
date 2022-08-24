''' pars message from vk '''
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkApi
from vk_api.utils import get_random_id
import json, random
import teleg_in

API_VERSION = "5.131"
GROUP_ID = "***"
GROUP_TOKEN = "***"
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()
peer_id = "2000000003"


def main():

    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    print("asd")
    for event in longpoll.listen():
        print("========================")
        print("Новое уведомление")
        print(event)
        print("========================")

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.message.peer_id)
            print(event.message.from_id)
            if event.message.peer_id == int(peer_id):
                request = event.message.text.lower()  
    
                print("==================")
                print('Сообщение:')
                print(f'от: {event.message.from_id}')
                print('Текст:', event.message.text)
                print("==================")
                name = ""
                
                if event.message.from_id == 134127477:
                    name = "LanS: "
                elif event.message.from_id == 287082324:
                    name = "AlSimakoff: "
                else: 
                    name = "No name: "
    
                message = name+event.message.text
                
                teleg_in.prinyalotvk(message)

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print("==================")
            print('Сообщение от тг:')
            print('Текст:', event.obj.text)
            print("==================")
   
        else:
            
            print(event)

if __name__ == '__main__':
    main()
