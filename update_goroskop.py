from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import bs4, random, requests, vk_api


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()

def goroscop1():
    spisok_znakov=['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
    for i in range (0,12):
        filegor=open('/root/bot_herobot_chat/resurses/goroskop_files/'+spisok_znakov[i]+'.txt','w')
        filegor.write(((bs4.BeautifulSoup(requests.get("http://astroscope.ru/horoskop/ejednevniy_goroskop/" + spisok_znakov[i] + ".html").text,"html.parser").find('div', 'col-12')).getText().lstrip()))
        filegor.close()
        
goroscop1()
vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    message='Гороскоп обновлен в фоновом режиме'
    )