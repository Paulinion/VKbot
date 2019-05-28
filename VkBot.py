import requests
import vk_api

vk_session = vk_api.VkApi(token='56f368dfcaed16f54ac92d85b3e27c51c370c74e5e6980cd2e3d64cb05ed10f0f9c88b9fc641810bb35cc')
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
        if event.text == 'очередь' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='ещё не готово'
		)
