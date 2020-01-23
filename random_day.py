from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
import random, requests, vk_api, time


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)


spisok_chata = {195310233:"Никита Михайлов",38375746:"Антон Фокин",120727528:"Ольга Меркулова",51556033:"Петр Евдокимов",
                  13069991:"Андрей Петранов",20765196:"Катя Горюнова",109828457:"Александр Маслов",206947265:"Fidl Di-Di",
                  12403758:"Вика Карпеева",135053737:"Анастасия Живых"}
pidor_id = random.choice(list(spisok_chata.keys()))
pidor = spisok_chata[pidor_id]

f1 = open('resurses/pidors.txt', 'a')
f1.write(str(pidor_id)+'\n')

f1.close()

f1 = open('resurses/pidor_today.txt', 'w')
f1.write(str(pidor))
f1.close()

vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    message='Пидор дня обновлен в фоновом режиме, это [id' + str(pidor_id) + '|' + pidor + "]"
)

attachments = []
image_url = 'https://pp.userapi.com/c621701/v621701407/73af/RYLX4AO4K7s.jpg'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    attachment=','.join(attachments),
    message="Так-так-так, у нас ежедневная рубрика!"
)
time.sleep(10)
vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    message="Вот это неожиданность, оказывается, что ..."
)
time.sleep(10)
vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    message="[id"+str(pidor_id)+'|'+pidor+"] Ты пидор дня."
)
