#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time, datetime, bs4, random, requests, vk_api

print(vk_api.__version__)

smile = {"1": "𝟭", "2": "𝟮", "3": "𝟯", "4": "𝟰", "5": "𝟱", "6": "𝟲", "7": "𝟳", "8": "𝟴", "9": "𝟵", "0": "𝟬"}
dict = [".", ",", "!", "?", ")", "(", ":", ";", "'", ']', '[', '"']
dictan = [")", "(", ":", ";", "'", ']', '[', '"', '\\', 'n', '&', 'q', 'u', 'o', 't']
dict2 = ["пидр", "сука", "лох", "пидрила", "мудак", "дурак", "тупой", "тормоз", "дебил", "дибил", "дурачок"]
dict4 = ["кушать", "пить", "есть", "поесть", "жрать"]
dict5 = ["вик", "ксюх", "ксюш", "ксень", "саш", "сань", "петь", "петя", "петро", "кать",
         "катя", "катюх", "андрей", "андрюх", "оля", "оль", "ник"]
dict7 = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}
dict8 = {'овен': 'aries', 'телец': 'taurus', 'близнецы': 'gemini', 'рак': 'cancer', 'лев': 'leo', 'дева': 'virgo',
         'весы': 'libra', 'скорпион': 'scorpio', 'стрелец': 'sagittarius', 'козерог': 'capricorn',
         'водолей': 'aquarius', 'рыбы': 'pisces'}
im_text={'Переменная облачность':'⛅','Облачно с прояснениями':'⛅','Небольшая облачность':'⛅',
         'Сплошная облачность':'☁','Ясно':'☀'}
im_text_2={'дождь':'💧','снег':'❄'}
kolresp = 0
attachments = []
chand = 0
flagtime = False
fltm1 = False
fltm2 = False
flaggoroscop = False

session = requests.Session()
vk_session = vk_api.VkApi(token='705c3fcc0cfb0bdcf449d510b3ec247f114169fefc6166dcdd6e0103c9149ed6348f60178513c0b4aadae')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

keyboard1 = VkKeyboard(one_time=False)
keyboard1.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard1.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard1.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)

keyboard2 = VkKeyboard(one_time=False)
keyboard2.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()  # Переход на вторую строку
keyboard2.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Факт', color=VkKeyboardColor.PRIMARY)

keyboard3 = VkKeyboard(one_time=False)
keyboard3.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()  # Переход на вторую строку
keyboard3.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Факт', color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button('Отстань', color=VkKeyboardColor.NEGATIVE)
keyboard3.add_button('Вернись', color=VkKeyboardColor.POSITIVE)
'''
for i in range(2,10):
    vk.messages.send(
        chat_id=i,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Поправлена клавиатура, изменен синтаксис команд (список доступен по команде "!help / !хелп / !помощь"), поправлена погода'
    )

vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    keyboard=keyboard.get_keyboard(),
    message=''
)
'''


def goroscop1():
    spisok_znakov = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius',
                     'capricorn', 'aquarius', 'pisces']
    for i in range(0, 12):
        f = requests.get(
            "http://astroscope.ru/horoskop/ejednevniy_goroskop/" + spisok_znakov[i] + ".html")  # .text,"html.parser"
        f.encoding = 'utf-8'
        text_gor = (bs4.BeautifulSoup(f.text, "html.parser").find('div', 'col-12'))
        #print(str(str(text_gor).split('\n')[2]).lstrip())
        filegor = open('/root/bot_herobot_chat/resurses/goroskop_files/' + spisok_znakov[i] + '.txt', 'w')  # /root/bot_herobot_chat
        filegor.write(str(str(text_gor).split('\n')[2]).lstrip())
        filegor.close()


def goroscop(bd_date):
    if bd_date[1] == '1':
        if int(bd_date[0]) < 20:
            return 'capricorn'
        else:
            return 'aquarius'
    if bd_date[1] == '2':
        if int(bd_date[0]) < 19:
            return 'aquarius'
        else:
            return 'pisces'
    if bd_date[1] == '3':
        if int(bd_date[0]) < 21:
            return 'pisces'
        else:
            return 'aries'
    if bd_date[1] == '4':
        if int(bd_date[0]) < 21:
            return 'aries'
        else:
            return 'taurus'
    if bd_date[1] == '5':
        if int(bd_date[0]) < 21:
            return 'taurus'
        else:
            return 'gemini'
    if bd_date[1] == '6':
        if int(bd_date[0]) < 22:
            return 'gemini'
        else:
            return 'cancer'
    if bd_date[1] == '7':
        if int(bd_date[0]) < 23:
            return 'cancer'
        else:
            return 'leo'
    if bd_date[1] == '8':
        if int(bd_date[0]) < 23:
            return 'leo'
        else:
            return 'virgo'
    if bd_date[1] == '9':
        if int(bd_date[0]) < 23:
            return 'virgo'
        else:
            return 'libra'
    if bd_date[1] == '10':
        if int(bd_date[0]) < 23:
            return 'libra'
        else:
            return 'scorpio'
    if bd_date[1] == '11':
        if int(bd_date[0]) < 22:
            return 'scorpio'
        else:
            return 'sagittarius'
    if bd_date[1] == '12':
        if int(bd_date[0]) < 22:
            return 'sagittarius'
        else:
            return 'capricorn'


def wheather(city, zavtra, zavtra_1):
    for i in range(len(city)):
        if city[i] == ' ':
            city = city[:i:] + '-' + city[i + 1::]
    request = requests.get("https://sinoptik.com.ru/погода-" + city)
    b = bs4.BeautifulSoup(request.text, "html.parser")
    #print(b)
    try:
        article = b.find_all("div", "weather__article_description-text")
        temperature = b.find_all("div", "table__temp")
        image = b.find_all("div","table__time_img")
        wind = b.find_all("div", "table__wind")
        #print(image)

        weather1 = temperature[0 + zavtra].getText()

        image1=image[0].getText()
        image1_1=''
        for i in image1:
            if i != '\n':
                image1_1 += i
        image1 = image1_1
        image1 = image1.split(', ')
        cloud1 = im_text[image1[0]]
        if len(image1) == 2:
            if image1[1].find("снег") != -1:
                rain1 = im_text_2["снег"]
            if image1[1].find("дождь") != -1:
                rain1 = im_text_2["дождь"]
        else: rain1=''
        #print(cloud1,rain1)

        wind1 = ''
        wind1 += str(wind[0 + zavtra]).split(' ')[3][7:-5:1] + ', '
        wind1 += wind[0 + zavtra].getText() + ' м/с.'
        wind1 = wind1.split(' ')
        wind1 = wind1[1::]
        wind1[0] = wind1[0].split('\n')
        wind1[0] = ''.join(wind1[0][-1::])
        wind1 = ' '.join(wind1[:-1:])
        wind1_1 = ''
        for i in wind1:
            if i != '\n':
                wind1_1 += i

        weather2 = temperature[2 + zavtra].getText()

        image2 = image[2].getText()
        image2_1 = ''
        for i in image2:
            if i != '\n':
                image2_1 += i
        image2 = image2_1
        image2 = image2.split(', ')
        cloud2 = im_text[image2[0]]
        if len(image2) == 2:
            if image2[1].find("снег") != -1:
                rain2 = im_text_2["снег"]
            if image2[1].find("дождь") != -1:
                rain2 = im_text_2["дождь"]
        else:
            rain2 = ''
        #print(cloud2, rain2)

        wind2 = ''
        wind2 += str(wind[2 + zavtra]).split(' ')[3][7:-5:1] + ', '
        wind2 += wind[2 + zavtra].getText() + ' м/с.'
        wind2 = wind2.split(' ')
        wind2 = wind2[1::]
        wind2[0] = wind2[0].split('\n')
        wind2[0] = ''.join(wind2[0][-1::])
        wind2 = ' '.join(wind2[:-1:])
        wind2_1 = ''
        for i in wind2:
            if i != '\n':
                wind2_1 += i

        weather3 = temperature[4 + zavtra].getText()

        image3 = image[4].getText()
        image3_1 = ''
        for i in image3:
            if i != '\n':
                image3_1 += i
        image3 = image3_1
        image3 = image3.split(', ')
        cloud3 = im_text[image3[0]]
        if len(image3) == 2:
            if image3[1].find("снег") != -1:
                rain3 = im_text_2["снег"]
            if image3[1].find("дождь") != -1:
                rain3 = im_text_2["дождь"]
        else:
            rain3 = ''
        #print(cloud3, rain3)

        wind3 = ''
        wind3 += str(wind[4 + zavtra]).split(' ')[3][7:-5:1] + ', '
        wind3 += wind[4 + zavtra].getText() + ' м/с.'
        wind3 = wind3.split(' ')
        wind3 = wind3[1::]
        wind3[0] = wind3[0].split('\n')
        wind3[0] = ''.join(wind3[0][-1::])
        wind3 = ' '.join(wind3[:-1:])
        wind3_1 = ''
        for i in wind3:
            if i != '\n':
                wind3_1 += i

        weather4 = temperature[6 + zavtra].getText()

        image4 = image[6].getText()
        image4_1 = ''
        for i in image4:
            if i != '\n':
                image4_1 += i
        image4 = image4_1
        image4 = image4.split(', ')
        cloud4 = im_text[image4[0]]
        if len(image4) == 2:
            if image4[1].find("снег") != -1:
                rain4 = im_text_2["снег"]
            if image4[1].find("дождь") != -1:
                rain4 = im_text_2["дождь"]
        else:
            rain4 = ''
        #print(cloud4, rain4)

        wind4 = ''
        wind4 += str(wind[6 + zavtra]).split(' ')[3][7:-5:1] + ', '
        wind4 += wind[6 + zavtra].getText() + ' м/с.'
        wind4 = wind4.split(' ')
        wind4 = wind4[1::]
        wind4[0] = wind4[0].split('\n')
        wind4[0] = ''.join(wind4[0][-1::])
        wind4 = ' '.join(wind4[:-1:])
        wind4_1 = ''
        for i in wind4:
            if i != '\n':
                wind4_1 += i

        result = ''
        if zavtra == 8:
            result += "Погода на завтра в городе " + city.capitalize() + ':\n\n'
        result = result + ('Ночью : ' + cloud1 + rain1 + ' ' + weather1 + ',\nВетер: ' + wind1_1 + '.') + '\n\n'
        result = result + ('Утром : ' + cloud2 + rain2 + ' ' + weather2 + ',\nВетер: ' + wind2_1 + '.') + '\n\n'
        result = result + ('Днём : ' + cloud3 + rain3 + ' ' + weather3 + ',\nВетер: ' + wind3_1 + '.') + '\n\n'
        result = result + ('Вечером : ' + cloud4 + rain4 + ' ' + weather4 + ',\nВетер: ' + wind4_1 + '.') + 2 * '\n'
        result += article[0 + zavtra_1].getText()
        return result
    except IndexError:
        return 'Такого города не найдено'


def mainfunc():
    flagtime = False
    fltm1 = False
    fltm2 = False
    try:
        for event in longpoll.listen():
            attachments = []
            flkv = False
            flkv2 = False
            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:

                # преобразование текста сообщения
                kupi_slona = event.obj.text
                event.obj.text = event.obj.text.lower();
                evtxt = ''
                for i in range(0, len(event.obj.text)):
                    if not event.obj.text[i] in dict or (i == 0 and event.obj.text[i] == '!'):
                        evtxt += event.obj.text[i]
                if evtxt == '':
                    event.obj.text = event.obj.text
                else:
                    event.obj.text = evtxt
                if event.obj.text[:24:] == 'club178949259|ботхеработ':
                    event.obj.text = event.obj.text[25::]
                    flkv = True

                if event.obj.text[:28:] == 'club178949259|@club178949259':
                    event.obj.text = event.obj.text[29::]
                    flkv2 = True

                # получение даты рождения, имени и фамилии
                if event.from_chat and event.obj.from_id != -183679552:
                    print(event)
                    fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
                        event.obj.from_id) + "&fields=bdate, city&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
                    first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
                    last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
                    try:
                        proverochka = fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower()
                        flagbddate = True
                        bd_date = fio.text[14::].split(',')[5].split(':')[1][1:-1:]
                    except:
                        try:
                            flagbddate = True
                            bd_date = fio.text[14::].split(',')[5].split(':')[1][1:-4:]
                        except:
                            flagbddate = False
                            bd_date = None

                    # запись сообщения в лог файл
                    s = open('logs_chat.txt', 'a')
                    s.write(last_name + ' *_* ' + first_name + ' *_* ' + str(event.obj.from_id) + ' *_* ' + str(
                        event.chat_id) + ' *_* ' + kupi_slona + '\n')
                    s.close()

                    # получение текущего дня
                    if time.strftime("%d", time.localtime())[0] == '0':
                        den = time.strftime("%d", time.localtime())[1::]
                    else:
                        den = time.strftime("%d", time.localtime())

                    # проверка на поздравление с др и поздравление
                    pozdrflag = False
                    pozdr = open('resurses/pozdravlenie.txt', 'r')
                    for i in pozdr:
                        if str(event.obj.from_id) == i[:-1:]:
                            pozdrflag = True
                    pozdr.close()
                    if flagbddate == True and str(dict7[time.strftime("%B", time.localtime())]) == bd_date.split('.')[
                        1] and den == \
                            bd_date.split('.')[0] and pozdrflag is False:
                        pozdr = open('resurses/pozdravlenie.txt', 'a')
                        pozdr.write(str(event.obj.from_id) + '\n')
                        pozdr.close()
                        image_url = 'https://pp.userapi.com/c850128/v850128497/10e229/uPpRrYrMR-4.jpg'
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message="О, " + first_name + ", Поздравляю тебя с Днём Рождения! 💐💐💐\nМоё железное сердце всегда радуется твоим сообщениям!"
                        )

                    # флаг на обращение к конкретному пользователю, бот игнорирует, если True
                    flagobr = 0
                    for i in range(len(dict5)):
                        if event.obj.text.find(dict5[i]) != -1:
                            flagobr = 1

                    # флаг на триггер к картинке "пить"
                    flag3 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        for k in dict4:
                            if k == str(event1[i]):
                                if event.obj.text.find('хочешь') != -1 or event.obj.text.find(
                                        'будем') != -1 or event.obj.text.find('будешь') != -1 \
                                        or event.obj.text.find('пошли') != -1 or event.obj.text.find(
                                    'где') != -1 or event.obj.text.find('го') != -1 \
                                        or event.obj.text.find('погнали') != -1 or event.obj.text.find(
                                    'куда') != -1 or event.obj.text.find('гоу') != -1 and k == 'есть':
                                    flag3 = 1
                                    flag2 = k
                                else:
                                    if k != 'есть':
                                        flag3 = 1
                                        flag2 = k

                    # флаг на матные  слова в тексте сообщения, подсчет их количества
                    flag1 = 0
                    kol_mat_in_text = 0
                    sp_mat = []
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        mat = open('resurses/matsp1.txt', mode='r')
                        for k in mat:
                            if str(event1[i]) == k[:-1:] and (k[:-1:] not in sp_mat):
                                sp_mat.append(k[:-1:])
                                flag1 = 1
                                kol_mat_in_text += 1
                        mat.close()

                    # флаг на фразу "пиздуй учиться"
                    flag10 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        if str(event1[i]) == 'лень' or str(event1[i]) == 'лениво' or str(event1[i]) == 'учиться' or str(
                                event1[i]) == 'ботать':
                            flag10 = 1

                    # флаг на фразу "сам такой"
                    flag = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(dict2)):
                        for k in range(0, len(event1)):
                            if event1[k] == dict2[i]:
                                flag = 1
                                flag2 = i

                    # обработка мата в сообщении
                    if flag1 == 1 and event.obj.text.find('!отъебись') == -1 and event.obj.text.find('! пидоры') == -1 \
                            and event.obj.text.find('! пидор дня') == -1:
                        for i in range(0, kol_mat_in_text):
                            f1 = open('resurses/mat.txt', 'a')
                            f1.write(str(event.obj.from_id) + '\n')
                            f1.close()
                        f1 = open('resurses/mat.txt', 'r')
                        chmat = 0
                        for line in f1:
                            if line == str(event.obj.from_id) + '\n':
                                chmat += 1
                        try:
                            vk.messages.send(
                                user_id=event.obj.from_id,
                                random_id=get_random_id(),
                                message='Теперь у тебя ' + str(
                                    chmat) + ' грязных словечек в чате, я всё вижу, ' + first_name + "."
                            )
                            f1.close()
                        except vk_api.exceptions.VkApiError:
                            vk.messages.send(
                                user_id=195310233,
                                random_id=get_random_id(),
                                message='Возникла ошибка в доступе к личным сообщениям, id пользователя ' + str(
                                    event.obj.from_id) + ' имя пользователя ' + first_name + ' ' + last_name
                            )
                            f1.close()

                    # обработка команды помощи
                    elif (event.obj.text == '!help' or event.obj.text == "!помощь" or event.obj.text == "!хелп" or
                          event.obj.text == '! help' or event.obj.text == "! помощь" or event.obj.text == "! хелп") \
                            and (event.chat_id == 1):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Привет! В Беседах мне доступны следующие функции:\n1) !погода\n2) !погода в городе ...\n'
                                    '3) !погода на завтра в городе ...\n4) !погода на завтра\n5) !кубик ...\n6) !гороскоп\n'
                                    '7) !анекдот\n8) !цитата\n9) !факт\n10) !мысль\n11) купи слона\n'
                                    '12) !пидор дня\n13) !пидоры\n14) !отстань, !отъебись, !вернись\n15) !крокодил\n16) !крокодил стата\n'
                                    'Остальное время я буду просто реагировать на некоторые контекстные фразы'
                        )
                    elif (event.obj.text == '!help' or event.obj.text == "!помощь" or event.obj.text == "!хелп" or
                          event.obj.text == '! help' or event.obj.text == "! помощь" or event.obj.text == "! хелп") \
                            and (event.chat_id != 1):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Привет! В Беседах мне доступны следующие функции:\n1) !погода\n2) !погода в городе ...\n'
                                    '3) !погода на завтра в городе ...\n4) !погода на завтра\n5) !кубик ...\n6) !гороскоп\n'
                                    '7) !анекдот\n8) !цитата\n9) !факт\n10) !мысль\n11) купи слона\n12) !крокодил\n13) !крокодил стата\n'
                                    'Остальное время я буду просто реагировать на некоторые контекстные фразы'
                        )

                    # обработка клавиатур для чатов
                    elif (event.obj.text == '!клавиатура1 вкл' or event.obj.text == '!клавиатура вкл' or
                          event.obj.text == '! клавиатура1 вкл' or event.obj.text == '! клавиатура вкл'):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboard1.get_keyboard(),
                            message='Клавиатура тип 1 включена'
                        )
                    elif (event.obj.text == '!клавиатура2 вкл' or event.obj.text == '! клавиатура2 вкл'):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboard2.get_keyboard(),
                            message='Клавиатура тип 2 включена'
                        )
                    elif (event.obj.text == '!клавиатура3 вкл' or event.obj.text == '! клавиатура3 вкл'):
                        if event.chat_id == 1:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                keyboard=keyboard3.get_keyboard(),
                                message='Клавиатура тип 3 включена'
                            )
                        else:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='Данный тип клавиатуры не доступен в этом чате'
                            )
                    elif (event.obj.text == '!клавиатура выкл' or event.obj.text == '! клавиатура выкл'):
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboard1.get_empty_keyboard(),
                            message='Клавиатура выключена'
                        )

                    # обработка выключения бота на время (нужно доделать для разных чатов)
                    elif (event.obj.text == '!отъебись' or event.obj.text == '! отъебись') and event.chat_id == 1:
                        fltm1 = False
                        stoptime2 = time.time()
                        flagtime = True
                        fltm2 = True
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я ухожу, но обещаю вернуться!\n(На один час)'
                        )

                    elif (event.obj.text == '!отстань' or event.obj.text == '! отстань') and event.chat_id == 1 or\
                            event.obj.text == 'отстань' and flkv == True or event.obj.text == 'отстань' and flkv2 == True:
                        fltm2 = False
                        stoptime1 = time.time()
                        flagtime = True
                        fltm1 = True
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я ухожу, но обещаю вернуться!\n(На 10 минут)'
                        )

                    elif flagtime is True and (event.obj.text == '!вернись' or event.obj.text == '! вернись') and\
                            event.chat_id == 1 or flagtime is True and event.obj.text == 'вернись' and flkv == True or\
                            flagtime is True and event.obj.text == 'вернись' and flkv2 == True:
                        flagtime = False
                        fltm1 = False
                        fltm2 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )

                    elif flagtime is False and (event.obj.text == '!вернись' or event.obj.text == '! вернись') and \
                            event.chat_id == 1 or flagtime is False and event.obj.text == 'вернись' and flkv == True or \
                            flagtime is False and event.obj.text == 'вернись' and flkv2 == True:
                        flagtime = False
                        fltm1 = False
                        fltm2 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я и не уходил от Вас'
                        )

                    if fltm1 is True and flagtime is True and time.time() - stoptime1 >= 600:
                        flagtime = False
                        fltm1 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )

                    if fltm2 is True and flagtime is True and time.time() - stoptime2 >= 3600:

                        flagtime = False
                        fltm2 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )


                    elif flag == 1 and flagobr == 0 and flagtime != True:
                        vk.messages.send(  # Отправляем сообщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Сам такой, ' + dict2[flag2] + ', ' + last_name
                        )

                    # обработка срока армии Антона(нужно доделать прогресс бар)
                    elif event.obj.text == '!антон' or event.obj.text == '! антон':
                        aa = datetime.date.today()
                        bb = datetime.date(2020, 7, 3)
                        cc = bb - aa
                        dd = datetime.date(2019, 7, 5)
                        hh = aa - dd
                        dateAntonfinish = (str(cc).split(',')[0].split(' ')[0])
                        dateAntonstart = (str(hh).split(',')[0].split(' ')[0])

                        def Antontime(dateAnton):
                            dateAnton = str(dateAnton)
                            if dateAnton[-2::] == '12' or dateAnton[-2::] == '11' or dateAnton[
                                                                                     -2::] == '13' or dateAnton[
                                                                                                      -2::] == '14':
                                return 'дней.'
                            if dateAnton[-1] == '1':
                                return 'день.'
                            if dateAnton[-1] == '2' or dateAnton[-1] == '3' or dateAnton[-1] == '4':
                                return 'дня.'
                            if dateAnton[-1] == '0' or dateAnton[-1] == '5' or dateAnton[-1] == '6' or dateAnton[
                                -1] == '7' or dateAnton[-1] == '8' or dateAnton[-1] == '9':
                                return 'дней.'

                        percent = str(int(dateAntonstart) // 3.66)[:-2:]
                        progress_bar = ''
                        for i in range(1, 51):
                            if i <= int(percent) // 2:
                                progress_bar += '❙'
                            else:
                                progress_bar += '❘'
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Антон вернётся к нам через ' + str(dateAntonfinish) + ' ' + Antontime(
                                dateAntonfinish) + '\nОн уже служит ' + str(dateAntonstart) + ' ' + Antontime(
                                dateAntonstart) + '\nУже прошло ' + str(percent) + '% Aрмии.' + '\n' + progress_bar
                        )

                    # обработка однословных команд бота
                    elif event.obj.text == '!мысль' or event.obj.text == '! мысль' or\
                            event.obj.text == 'мысль' and flkv == True or event.obj.text == 'мысль' and flkv2 == True:
                        cit = random.randint(0, 1355)
                        for linenum, line in enumerate(open('resurses/quotes_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        keyboardquotes = VkKeyboard(one_time=False, inline=True)
                        keyboardquotes.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboardquotes.get_keyboard(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == '!факт' or event.obj.text == '! факт' or event.obj.text == 'факт' and\
                            flkv == True or event.obj.text == 'факт' and flkv2 == True:
                        cit = random.randint(0, 764)
                        for linenum, line in enumerate(open('resurses/facts_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        keyboardfacts = VkKeyboard(one_time=False, inline=True)
                        keyboardfacts.add_button('Факт', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboardfacts.get_keyboard(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == '!цитата' or event.obj.text == '! цитата' or event.obj.text == 'цитата' and\
                            flkv == True or event.obj.text == 'цитата' and flkv2 == True:
                        cit = random.randint(0, 1391)
                        for linenum, line in enumerate(open('resurses/twtrr.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        keyboardtwtrr = VkKeyboard(one_time=False, inline=True)
                        keyboardtwtrr.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboardtwtrr.get_keyboard(),
                            message=str(messagecit)
                        )


                    elif event.obj.text == '!анекдот' or event.obj.text == '! анекдот' or event.obj.text == 'анекдот' and\
                            flkv == True or event.obj.text == 'анекдот' and flkv2 == True:

                        anes = random.randint(0, 135500)
                        for linenum, line in enumerate(open('resurses/anec.txt', 'r')):
                            if linenum == anes:
                                anecdot = (line.strip()).replace('#', '\n')

                        keyboardanec = VkKeyboard(one_time=False, inline=True)
                        keyboardanec.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboardanec.get_keyboard(),
                            message=anecdot
                        )

                    elif (event.obj.text == '!обнови гороскоп' or event.obj.text == '! обнови гороскоп') and event.obj.from_id == 195310233:
                        goroscop1()
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='обновил'
                        )



                    elif (event.obj.text == '!крокодил стата' or event.obj.text == '! крокодил стата'):
                        f = open('/root/bot_herobot_chat/resurses/crocodile_files/stat.txt', 'r') #/root/bot_herobot_chat/
                        dism = {}
                        for line in f:
                            g=line.split("***")
                            if str(event.chat_id) == g[1][:-1:]:
                                if g[0] in dism:
                                    dism[g[0]] += 1
                                else:
                                    dism[g[0]] = 1
                        f.close()

                        mat = []
                        kolp = []
                        for i in dism:
                            kolp.append(dism[i])
                        kolp.sort()
                        kolp.reverse()
                        jstr = []
                        for i in kolp:
                            for j in dism:
                                if j == '' or j == '\n':
                                    continue
                                if str(dism[j]) == str(i) and j not in jstr:
                                    jstr.append(j)
                                    number_2 = ''
                                    for k in str(dism[j]):
                                        number_2 += smile[k]
                                    fio_1 = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(j)
                                                         + "&fields=bdate&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
                                    first_name_1 = fio_1.text[14::].split(',')[1].split(':')[1][1:-1:]
                                    last_name_1 = fio_1.text[14::].split(',')[2].split(':')[1][1:-1:]
                                    mat.append(first_name_1 + ' ' + last_name_1 + ': ' + str(number_2) + ' раз(а) угадал слово.\n')
                        for i in range(0, len(mat)):
                            mat[i] = str(i + 1) + ") " + mat[i]
                        mat = ''.join(mat)
                        mat = "🔝 ТОП крокодила:\n\n" + mat
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=mat
                        )

                    elif (event.obj.text == '!маты' or event.obj.text == '! маты'):
                        f = open('resurses/mat.txt', 'r')
                        dism = {}
                        for line in f:
                            if line in dism:
                                dism[line] += 1
                            else:
                                dism[line] = 1
                        f.close()
                        mat = []
                        kolp = []
                        for i in dism:
                            kolp.append(dism[i])
                        kolp.sort()
                        kolp.reverse()
                        jstr = []
                        for i in kolp:
                            for j in dism:
                                if j == '' or j == '\n':
                                    continue
                                if str(dism[j]) == str(i) and j not in jstr:
                                    jstr.append(j)
                                    number_2 = ''
                                    for k in str(dism[j]):
                                        number_2 += smile[k]
                                    fio_1 = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(j)[
                                                                                                           :-1:] + "&fields=bdate&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
                                    first_name_1 = fio_1.text[14::].split(',')[1].split(':')[1][1:-1:]
                                    last_name_1 = fio_1.text[14::].split(',')[2].split(':')[1][1:-1:]
                                    mat.append(first_name_1 + ' ' + last_name_1 + ': ' + str(number_2) + ' раз(а)\n')
                        for i in range(0, len(mat)):
                            mat[i] = str(i + 1) + ") " + mat[i]
                        mat = ''.join(mat)
                        mat = "🔝 ТОП мата:\n\n" + mat
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=mat
                        )

                    elif (event.obj.text == '!пидор дня' or event.obj.text == '! пидор дня') and (event.chat_id == 1 or event.chat_id == 5):
                        f1 = open('resurses/pidor_today.txt', 'r')
                        pidor_2 = f1.read()
                        f1.close()
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message="Сегодня пидор дня " + pidor_2
                        )

                    elif (event.obj.text == '!пидоры' or event.obj.text == '! пидоры') and (event.chat_id == 1 or event.chat_id == 5):
                        spisok_chata = {195310233: "Никита Михайлов",
                                        38375746: "Антон Фокин",
                                        120727528: "Ольга Меркулова",
                                        51556033: "Петр Евдокимов",
                                        13069991: "Андрей Петранов",
                                        20765196: "Катя Горюнова",
                                        109828457: "Александр Маслов",
                                        206947265: "Fidl Di-Di",
                                        12403758: "Вика Карпеева",
                                        135053737: "Анастасия Живых"}
                        pidors = open('resurses/pidors.txt', 'r')
                        dism = {}
                        for line in pidors:
                            if line in dism:
                                dism[line] += 1
                            else:
                                dism[line] = 1
                        pidors.close()
                        for i in spisok_chata:
                            if str(i) not in dism:
                                dism[i] = 0
                        pidors_1 = []
                        kolp = []
                        for i in dism:
                            kolp.append(dism[i])
                        kolp.sort()
                        kolp.reverse()
                        jstr = []
                        nstr = []
                        for i in kolp:
                            for j in dism:
                                if j == '' or j == '\n':
                                    continue
                                if str(dism[j]) == str(i) and j not in jstr and spisok_chata[int(j)] not in nstr:
                                    nstr.append(spisok_chata[int(j)])
                                    jstr.append(j)
                                    number_1 = ''
                                    for k in str(dism[j]):
                                        number_1 += smile[k]
                                    pidors_1.append(spisok_chata[int(j)] + ': ' + number_1 + ' раз(а)\n')

                        for i in range(0, len(pidors_1)):
                            pidors_1[i] = str(i + 1) + ") " + pidors_1[i]
                        pidors_1 = ''.join(pidors_1)
                        pidors_1 = "🔝 ТОП пидоров дня:\n\n" + pidors_1

                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=pidors_1
                        )

                    elif event.obj.text == '!гороскоп' or event.obj.text == '! гороскоп' or event.obj.text == 'гороскоп' and flkv == True or event.obj.text == 'гороскоп' and flkv2 == True:
                        if flagbddate == True:
                            bd_date = bd_date.split('.')
                            zodiak = goroscop(bd_date)
                            simbol_zodiak={'aries':'♈', 'taurus':'♉', 'gemini':'♊', 'cancer':'♋', 'leo':'♌','virgo':'♍',
                                           'libra':'♎', 'scorpio':'♏', 'sagittarius':'♐','capricorn':'♑', 'aquarius':'♒', 'pisces':'♓'}
                            f = open('resurses/goroskop_files/' + zodiak + '.txt', 'r')
                            goroskp = f.read()
                            f.close()
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=simbol_zodiak[zodiak]+' '+goroskp
                            )
                        else:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='У тебя нет даты Рождения ВК'
                            )


                    elif flag3 == 1 and flagobr == 0 and flagtime != True:
                        image_url = 'https://pp.userapi.com/c851020/v851020736/cb17f/BgYwz2bShuc.jpg'
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                                           )
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message='Кто сказал ' + flag2 + '?'
                        )

                    elif event.obj.text.find('!погода на завтра в городе') != -1 or event.obj.text.find('! погода на завтра в городе') != -1:
                        if event.obj.text.find('!погода на завтра в городе') != -1:
                            inder=27
                        else:
                            inder=28
                        tommor = str(datetime.date.today()).split('-')
                        tommor[-1] = str(int(tommor[-1]) + 1)
                        if len(str(int(tommor[-1]))) == 1:
                            tommor[-1] = "0" + str(int(tommor[-1]))
                        tommor = '-'.join(tommor)
                        city = event.obj.text[inder::] + '/' + tommor
                        print(city)
                        result = wheather(city, 0, 0)
                        result = "Погода на завтра в городе " + city.capitalize().split('/')[0] + ':\n\n' + result
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('!погода на завтра') != -1 or event.obj.text.find('! погода на завтра') != -1 or event.obj.text.find(
                            '☂ погода на завтра') != -1 and flkv == True or event.obj.text.find('☂ погода на завтра') != -1 and flkv2 == True:
                        try:
                            tommor = str(datetime.date.today()).split('-')
                            tommor[-1] = str(int(tommor[-1]) + 1)
                            if len(str(int(tommor[-1]))) == 1:
                                tommor[-1] = "0" + str(int(tommor[-1]))
                            tommor = '-'.join(tommor)
                            city = fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower() + '/' + tommor
                        except:
                            city = "москва"
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                            )
                        result = wheather(city, 0, 0)
                        result = "Погода на завтра в городе " + city.capitalize().split('/')[0] + ':\n\n' + result
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('!погода в городе') != -1 or event.obj.text.find('! погода в городе') != -1:
                        if event.obj.text.find('!погода в городе') != -1:
                            inder = 17
                        else:
                            inder = 18
                        city = event.obj.text[inder::]
                        result = wheather(city, 0, 0)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('!погода') != -1 or event.obj.text.find('! погода') != -1 or event.obj.text.find(
                            'погода') != -1 and flkv == True or event.obj.text.find('погода') != -1 and flkv2 == True:
                        try:
                            city = fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower()
                        except:
                            city = 'москва'
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                            )
                        keyboardweather = VkKeyboard(one_time=False, inline=True)
                        keyboardweather.add_button('☂ Погода на завтра', color=VkKeyboardColor.PRIMARY)
                        result = wheather(city, 0, 0)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=keyboardweather.get_keyboard(),
                            message=result
                        )

                    elif event.obj.text.find('купи слона') != -1 or event.obj.text.find('!купи слона') != -1:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Все говорят ' + kupi_slona + ', а ты купи слона'
                        )

                    elif event.obj.text.find('!кубик') != -1:
                        kub = event.obj.text[7::]
                        try:
                            vypalo = random.randint(1, int(kub))
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='Выпало число ' + str(vypalo)
                            )
                        except:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='С твоим числом что-то не так'
                            )

                    elif event.obj.text == 'ну и ладно' and flagtime != True:
                        image_url = 'https://pp.userapi.com/c851120/v851120719/d26d3/-orcQNPA2gI.jpg'
                        image = session.get(image_url, stream=True)
                        photo = upload.photo_messages(photos=image.raw)[0]
                        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                                           )
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=','.join(attachments),
                            message=''
                        )

                    elif event.obj.text.split(' ')[-1] == "нет" and flagtime != True:  # Если написали в Беседе
                        # print("чат", event.obj.text, event.chat_id)
                        k = ["Пидора ответ!", "Программиста ответ!", "Петика ответ!"]
                        a = random.randint(0, 2)
                        if random.randint(0, 1) == 1 and event.obj.from_id == 51556033:
                            a = 2
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=k[a]
                        )

                    elif flagtime != True and event.obj.text[-3::] == "300" or flagtime != True and event.obj.text[
                                                                                                    -6::] == "триста":  # Если написали в Беседе
                        # print("чат", event.obj.text, event.chat_id)
                        k = ["Отсоси у программиста!", "Отсоси у тракториста!", "Отвези домой таксиста!",
                             "Сам тащи рюкзак туриста", "Лизни подмышку пианиста"]
                        a = random.randint(0, 4)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=k[a]
                        )

                    elif event.obj.text.split(' ')[-1] == "бот" or event.obj.text == '!бот' and flagtime != True:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Херабот!'
                        )

                    elif flag10 == 1 and flagtime != True:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Пиздуй учиться, ' + first_name + '!'
                        )

                    elif flagtime != True and event.obj.text.split(' ')[-1] == "чо" or flagtime != True and \
                            event.obj.text.split(' ')[-1] == "че" or flagtime != True and event.obj.text.split(' ')[
                        -1] == "чё":
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Йух через плечо!'
                        )

                    elif event.obj.text.split(' ')[-1] == "да" and flagtime != True:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Сковорода!'
                        )

                    '''
                    else:

                        request = apiai.ApiAI('5223c3ee5b95429c8794b01faef6d4e5').text_request()
                        request.lang = 'ru'  # На каком языке будет послан запрос
                        request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
                        request.query = event.obj.text  # Посылаем запрос к ИИ с сообщением от юзера
                        # print(request.getresponse().read().decode('utf-8'))
                        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
                        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ

                        anssplit=open('baza3.txt','r')
                        for line in anssplit:
                            #print(event.obj.text,line.split('\\')[0])
                            if line.split('\\')[0]==event.obj.text:
                                response=line.split('\\')[1]
                                break
                            else:
                                response=None
                        anssplit.close()
                        anssplit=open('baza3.txt','r')
                        if response==None:
                            #print(11)
                            for line in anssplit:
                                for red in range (0,len(event.obj.text.split(' '))-1):
                                    if line.split('\\')[0].find(event.obj.text.split(' ')[red])!=-1:
                                        for green in range (0,len(event.obj.text.split(' '))-1):
                                            if line.split('\\')[0].find(event.obj.text.split(' ')[green])!=-1 and red!=green:
                                        #print(event.obj.text.split(' ')[red],line.split('\\')[0])
                                                response=line.split('\\')[1]
                                                break
                                            else:
                                                response=None

                                if response!=None:
                                    break
                        if response==None and random.randint(0,2)==2 and event.obj.text.isalpha() and len(event.obj.text)>6 and len(event.obj.text.split(' '))==1 and flagobr == 0 and flagtime != True:
                            xy=['ху','хуи','хуя','хуе']
                            t=random.randint(0,3)
                            t2=random.randint(3,4)
                            if len(event.obj.text.split(' '))==1 and kolresp >= random.randint(0, 5) and flagobr == 0 and flagtime != True:
                                vk.messages.send(
                                    chat_id=event.chat_id,
                                    random_id=get_random_id(),
                                    message=xy[t]+event.obj.text[-(t2)::]
                                )
                        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
                        if response and kolresp >= random.randint(0, 10) and flagobr == 0 and flagtime != True:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=response
                            )
                            kolresp = 0
                    kolresp += 1
                    '''
    except Exception as err:
        vk.messages.send(
            user_id=195310233,
            random_id=get_random_id(),
            message='Возникла ошибка ' + str(err) + ' в главном цикле bot_herobot_chat'
        )
        mainfunc()


mainfunc()

'''
                    elif event.obj.text == 'бот время':
                        hour = (time.strftime('%H', time.localtime()))
                        hour = int(hour)
                        tm1 = (time.strftime("Сегодня %B %d, %Y;", time.localtime()))
                        tm2 = (time.strftime(":%M", time.localtime()))
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=tm1 + ' ' + str(hour + 3) + tm2
                        )
'''
