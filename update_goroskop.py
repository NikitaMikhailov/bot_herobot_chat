from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
import requests
import vk_api
import bot_functions
import bot_variable

if bot_variable.flag_repository:
    start_path = ""
else:
    start_path = '/root/bot_herobot_chat/'

f = open('{}token.txt'.format(start_path), 'r')
token = f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
        
bot_functions.goroscop_update()

vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    message='Гороскоп обновлен в фоновом режиме.'
    )
