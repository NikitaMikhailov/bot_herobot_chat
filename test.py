'''
import requests
message_id=15938
rt = requests.get('https://api.vk.com/method/messages.delete?message_ids='+str(message_id)+'&delete_for_all=1&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92')
print(rt.text)
#--------------------------------------------------------------------------------------------------------------
f1 = open("resurses/crocodile_files/new1.txt",mode="w",encoding="utf-8")
f = open("resurses/crocodile_files/new.txt","r")
for line in f:
    line=line.split(" ")
    print(line[5][1:-1:])
    f1.write(line[5][1:-1:]+"\n")
f1.close()
f.close()
#-------------------------------------------------------------------------------------------------------------
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api, time, random
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

def sent_message_ls(text, user_id):
    message_ids = vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=text
    )
    return message_ids

sent_message_ls("&#8203;",195310233)
#-------------------------------------------------------------------------------------------------------------
import requests, json
message_id=15938
rt = requests.get('https://api.vk.com/method/messages.getConversationMembers?peer_id=2000000001&fields=count,items,profiles1&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92')
zapros = json.loads(rt.text)

for i in (zapros["response"]['profiles']):
    print(i['id'])
'''