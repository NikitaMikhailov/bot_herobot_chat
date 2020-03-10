from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import bs4, random, requests, vk_api


session = requests.Session()
vk_session = vk_api.VkApi(token='2956d05b8c9adc4484a001badf6a58db1a8377e650be4fe6a2aefc1f6fe4db011f184e71dbf82dd3b96a9')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()

def goroscop1():
    spisok_znakov=['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
    for i in range (0,12):

        f=requests.get("http://astroscope.ru/horoskop/ejednevniy_goroskop/" + spisok_znakov[i] + ".html")#.text,"html.parser"
        #print(f.encoding)
        f.encoding = 'utf-8'
        #print(f.text)
        text_gor=(bs4.BeautifulSoup(f.text,"html.parser").find('div', 'col-12'))
        print(str(str(text_gor).split('\n')[2]).lstrip())
        filegor=open('/root/bot_herobot_chat/resurses/goroskop_files/'+spisok_znakov[i]+'.txt','w')  #/root/bot_herobot_chat
        filegor.write(str(str(text_gor).split('\n')[2]).lstrip())
        filegor.close()
        
goroscop1()
vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    message='Гороскоп обновлен в фоновом режиме'
    )
