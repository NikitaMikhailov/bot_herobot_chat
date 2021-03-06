#! / Bin / sh
#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/bin/sh -
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import time, datetime, bs4, random, requests, vk_api


dict = [".", ",", "!", "?", ")", "(", ":", ";", "'", ']', '[', '"']
dictan = [")", "(", ":", ";", "'", ']', '[', '"', '\\', 'n', '&', 'q', 'u', 'o', 't']
dict2 = ["пидр", "сука", "лох", "пидрила", "мудак", "дурак", "тупой", "тормоз", "дебил", "дибил","дурачок"]
dict4 = ["кушать", "пить", "есть", "поесть", "жрать"]
dict5 = ["вик", "ксюх", "ксюш", "ксень", "саш", "сань", "петь", "петя", "петро", "кать",
         "катя", "катюх", "андрей", "андрюх", "оля", "оль", "ник"]
dict7 = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}
dict8 = {'овен':'aries','телец':'taurus' ,'близнецы':'gemini' ,'рак':'cancer' ,'лев':'leo' ,'дева':'virgo' ,'весы':'libra' ,'скорпион':'scorpio' ,'стрелец':'sagittarius','козерог':'capricorn' ,'водолей':'aquarius' ,'рыбы':'pisces'}
kolresp = 0
attachments = []
chand = 0
flagtime = False
fltm1 = False
fltm2 = False
flaggoroscop=False


session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
'''
keyboard.add_line()  # Переход на вторую строку
keyboard.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Факт', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Отстань', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Вернись', color=VkKeyboardColor.POSITIVE)

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
        filegor = open('resurses/goroskop_files/' + spisok_znakov[i] + '.txt', 'w')
        filegor.write(((bs4.BeautifulSoup(
            requests.get("http://astroscope.ru/horoskop/ejednevniy_goroskop/" + spisok_znakov[i] + ".html").text,
            "html.parser").find('div', 'col-12')).getText().lstrip()))
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

def wheather(city,zavtra,zavtra_1):
    for i in range(len(city)):
        if city[i] == ' ':
            city = city[:i:] + '-' + city[i + 1::]
    request = requests.get("https://sinoptik.com.ru/погода-" + city)
    b = bs4.BeautifulSoup(request.text, "html.parser")

    try:
        article=b.find_all("div","weather__article_description-text")
        temperature = b.find_all("div","table__temp")
        wind=b.find_all("div","table__wind")
        #print(wind)

        weather1 = temperature[0+zavtra].getText()
        #print(weather1)
        wind1=''
        wind1+=str(wind[0+zavtra]).split(' ')[3][7:-5:1]+', '
        wind1+=wind[0+zavtra].getText()+' м/с.'
        wind1 = wind1.split(' ')
        wind1 = wind1[1::]
        wind1[0] = wind1[0].split('\n')
        wind1[0] = ''.join(wind1[0][-1::])
        wind1 = ' '.join(wind1[:-1:])
        wind1_1=''
        for i in wind1:
            if i!='\n':
                wind1_1+=i

        weather2 = temperature[2+zavtra].getText()
        wind2=''
        wind2+=str(wind[2+zavtra]).split(' ')[3][7:-5:1]+', '
        wind2+=wind[2+zavtra].getText()+' м/с.'
        wind2 = wind2.split(' ')
        wind2 = wind2[1::]
        wind2[0] = wind2[0].split('\n')
        wind2[0] = ''.join(wind2[0][-1::])
        wind2 = ' '.join(wind2[:-1:])
        wind2_1=''
        for i in wind2:
            if i!='\n':
                wind2_1+=i

        weather3 = temperature[4+zavtra].getText()
        wind3 = ''
        wind3 += str(wind[4+zavtra]).split(' ')[3][7:-5:1] + ', '
        wind3 += wind[4+zavtra].getText() + ' м/с.'
        wind3 = wind3.split(' ')
        wind3 = wind3[1::]
        wind3[0] = wind3[0].split('\n')
        wind3[0] = ''.join(wind3[0][-1::])
        wind3 = ' '.join(wind3[:-1:])
        wind3_1 = ''
        for i in wind3:
            if i != '\n':
                wind3_1 += i

        weather4 = temperature[6+zavtra].getText()
        wind4 = ''
        wind4 += str(wind[6+zavtra]).split(' ')[3][7:-5:1] + ', '
        wind4 += wind[6+zavtra].getText() + ' м/с.'
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
            result += "Погода на завтра в городе "+city.capitalize()+':\n\n'
        result = result + ('Ночью : ' + weather1 + ', Ветер: ' + wind1_1+'.') + '\n'
        result = result + ('Утром : ' + weather2 + ', Ветер: ' + wind2_1+'.') + '\n'
        result = result + ('Днём : ' + weather3 + ', Ветер: ' + wind3_1+'.') + '\n'
        result = result + ('Вечером : ' + weather4 + ', Ветер: ' + wind4_1+'.') + 2 * '\n'
        result+=article[0+zavtra_1].getText()
        return result
    except IndexError:
        return 'Такого города не найдено'


def mainfunc():

    attachments = []
    chand = 0
    flagtime = False
    fltm1 = False
    fltm2 = False
    #day_time=time.strftime("%d", time.localtime())
    try:
        for event in longpoll.listen():
            kolresp=0
            attachments = []
            flkv = False
            flkv2 = False
            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
                #print(event.chat_id)
                # преобразование текста сообщения
                kupi_slona=event.obj.text
                event.obj.text = event.obj.text.lower();
                evtxt = ''
                for i in range(0, len(event.obj.text)):
                    if not event.obj.text[i] in dict or (i == 0 and event.obj.text[i] == '!'):
                        evtxt += event.obj.text[i]
                if evtxt == '':
                    event.obj.text = event.obj.text
                else:
                    event.obj.text = evtxt
                print(evtxt)
                if event.obj.text[:24:] == 'club178949259|ботхеработ':
                    event.obj.text = event.obj.text[25::]
                    flkv = True

                if event.obj.text[:28:] == 'club178949259|@club178949259':
                    event.obj.text = event.obj.text[29::]
                    flkv2 = True




                if event.from_chat and event.obj.from_id!=-183679552:
                    fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
                        event.obj.from_id) + "&fields=bdate, city&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
                    first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
                    last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
                    #print(fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower())
                    #print(fio.text)
                    try:
                        proverochka=fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower()
                        flagbddate=True
                        bd_date = fio.text[14::].split(',')[5].split(':')[1][1:-1:]
                        #print(bd_date)
                    except:
                        try:
                            flagbddate=True
                            bd_date = fio.text[14::].split(',')[5].split(':')[1][1:-4:]
                            #print(bd_date)
                        except:
                            flagbddate=False
                            bd_date=None
                    '''
                    print(time.strftime("%d", time.localtime()),day_time)

                    if day_time is None:
                        day_time=time.strftime("%d", time.localtime())

                    if time.strftime("%d", time.localtime())!=day_time:
                        date_file=open('anton.txt','r')
                        k = 0
                        for line in date_file:
                            if k == 0:
                                date_anton = int(line[0]) - 1
                            k += 1
                        date_file.close()
                        date_file=open('anton.txt','w')
                        date_file.write(date_anton)
                        date_file.close()
                        day_time=time.strftime("%d", time.localtime())
                    '''
                    s=open('logs_chat.txt','a')
                    s.write(last_name + ' *_* ' + first_name + ' *_* ' + str(event.obj.from_id) + ' *_* ' + str(event.chat_id) + ' *_* ' + kupi_slona + '\n')
                    s.close()

                    if time.strftime("%d", time.localtime())[0] == '0':
                        den = time.strftime("%d", time.localtime())[1::]
                    else:
                        den = time.strftime("%d", time.localtime())
                    # print(den,bd_date.split('.')[0])

                    pozdrflag = False
                    pozdr = open('resurses/pozdravlenie.txt', 'r')
                    for i in pozdr:
                        if str(event.obj.from_id) == i[:-1:]:
                            pozdrflag = True
                    pozdr.close()
                    if flagbddate==True and str(dict7[time.strftime("%B", time.localtime())]) == bd_date.split('.')[1] and den == \
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
                            message="О, " + first_name + ", Поздравляю тебя с Днём Рождения! Моё железное сердце всегда радуется твоим сообщениям!"
                        )

                    flagobr = 0
                    for i in range(len(dict5)):
                        if event.obj.text.find(dict5[i]) != -1:
                            flagobr = 1

                    flag3 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        for k in dict4:
                            if k == str(event1[i]):
                                if event.obj.text.find('хочешь')!=-1 or event.obj.text.find('будем')!=-1 or event.obj.text.find('будешь')!=-1\
                                        or event.obj.text.find('пошли')!=-1 or event.obj.text.find('где')!=-1 or event.obj.text.find('го')!=-1 \
                                        or event.obj.text.find('погнали')!=-1 or event.obj.text.find('куда')!=-1 or event.obj.text.find('гоу')!=-1 and k=='есть':
                                    flag3 = 1
                                    flag2 = k
                                else:
                                    if k!='есть':
                                        flag3 = 1
                                        flag2 = k

                    flag1 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        mat = open('resurses/matsp1.txt', 'r')
                        for k in mat:
                            if str(event1[i]) == k[:-1:]:
                                flag1 = 1
                        mat.close()

                    flag10 = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(event1)):
                        if str(event1[i]) == 'лень' or str(event1[i]) == 'лениво' or str(event1[i]) == 'учиться' or str(
                                event1[i]) == 'ботать':
                            flag10 = 1

                    flag = 0
                    event1 = event.obj.text.split(' ')
                    for i in range(len(dict2)):
                        for k in range(0, len(event1)):
                            if event1[k] == dict2[i]:
                                flag = 1
                                flag2 = i


                    if flag1 == 1 and event.obj.text.find('!отъебись') == -1:
                        f1 = open('resurses/mat.txt', 'a')
                        f1.write(str(event.obj.from_id))
                        f1.write('\n')
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
                                message='Это твоё ' + str(chmat) + ' грязное словечко в чате, я всё вижу, ' + first_name
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

                    elif event.obj.text == '!help' or event.obj.text == "!помощь" or event.obj.text == "!хелп":
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Привет! В Беседах мне доступны следующие функции:\n1) !погода\n2) !погода в городе ...\n'
                                    '3) !погода на завтра в городе ...\n4) !погода на завтра\n5) !анекдот\n6) !цитатa\n'
                                    '7) !кубик ...\n8) !гороскоп\n9) купи слона\n10) !мысль\n11) !факт\n'
                                    '12) !пидор дня\n13) !пидоры\n'
                                    'Остальное время я буду просто реагировать на некоторые контекстные фразы'
                        )

                    elif event.obj.text == '!отъебись' and event.chat_id==1:
                        fltm1 = False
                        stoptime2 = time.time()
                        flagtime = True
                        fltm2 = True
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я ухожу, но обещаю вернуться!\n(На один час)'
                        )

                    elif event.obj.text == '!отстань'  and event.chat_id==1 or event.obj.text == 'отстань' and flkv == True or event.obj.text == 'отстань' and flkv2 == True:
                        fltm2 = False
                        stoptime1 = time.time()
                        flagtime = True
                        fltm1 = True
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я ухожу, но обещаю вернуться!\n(На 10 минут)'
                        )

                    elif flagtime is True and event.obj.text == '!вернись'  and event.chat_id==1 or flagtime is True and event.obj.text == 'вернись' and flkv == True or flagtime is True and event.obj.text == 'вернись' and flkv2 == True:
                        flagtime = False
                        fltm1 = False
                        fltm2 = False
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Я вернулся!'
                        )

                    elif flagtime is False and event.obj.text == '!вернись'  and event.chat_id==1 or flagtime is False and event.obj.text == 'вернись' and flkv == True or flagtime is False and event.obj.text == 'вернись' and flkv2 == True:
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


                    elif event.obj.text == '!антон':
                        aa = datetime.date.today()
                        bb = datetime.date(2020,7,3)
                        cc=bb-aa
                        dd=datetime.date(2019,7,5)
                        hh=aa-dd
                        dateAntonfinish=(str(cc).split(',')[0].split(' ')[0])
                        dateAntonstart=(str(hh).split(',')[0].split(' ')[0])

                        def Antontime(dateAnton):
                            dateAnton=str(dateAnton)
                            if dateAnton[-2::]=='12' or dateAnton[-2::]=='11' or dateAnton[-2::]=='13' or dateAnton[-2::]=='14':
                                return 'дней.'
                            if dateAnton[-1]=='1':
                                return 'день.'
                            if dateAnton[-1]=='2' or dateAnton[-1]=='3' or dateAnton[-1]=='4':
                                return 'дня.'
                            if  dateAnton[-1]=='0' or dateAnton[-1]=='5' or dateAnton[-1]=='6' or dateAnton[-1]=='7' or dateAnton[-1]=='8' or dateAnton[-1]=='9':
                                return 'дней.'
                        percent = str(int(dateAntonstart) // 3.66)[:-2:]
                        progress_bar = ''
                        for i in range(1,51):
                            if i<=int(percent)//2:
                                progress_bar += '❙'
                            else:
                                progress_bar += '❘'
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='Антон вернётся к нам через ' + str(dateAntonfinish) + ' ' + Antontime(dateAntonfinish) + '\nОн уже служит ' + str(dateAntonstart) + ' ' + Antontime(dateAntonstart) + '\nУже прошло ' + str(percent) + '% Aрмии.'+'\n'+progress_bar
                        )

                    elif event.obj.text == '!мысль' or event.obj.text == 'мысль' and flkv == True or event.obj.text == 'мысль' and flkv2 == True:
                        cit = random.randint(0, 1355)
                        for linenum, line in enumerate(open('resurses/quotes_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == '!факт' or event.obj.text == 'факт' and flkv == True or event.obj.text == 'факт' and flkv2 == True:
                        cit = random.randint(0, 764)
                        for linenum, line in enumerate(open('resurses/facts_clear.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )

                    elif event.obj.text == '!цитата' or event.obj.text == 'цитата' and flkv == True or event.obj.text == 'цитата' and flkv2 == True:
                        cit = random.randint(0, 1391)
                        for linenum, line in enumerate(open('resurses/twtrr.txt', 'r')):
                            if linenum == cit:
                                messagecit = (line.strip())
                        if messagecit[-1] == ',':
                            messagecit = messagecit[:-1:]
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=str(messagecit)
                        )
                    elif event.obj.text == '!обнови гороскоп' and event.obj.from_id == 195310233:
                        goroscop1()
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message='обновил'
                        )

                    elif event.obj.text == '!пидор дня' and event.chat_id == 1:
                        f1 = open('resurses/pidor_today.txt', 'r')
                        pidor_2 = f1.read()
                        f1.close()
                        vk.messages.send(
                            chat_id=1,
                            random_id=get_random_id(),
                            message="Сегодня пидор дня "+pidor_2
                        )

                    elif event.obj.text == '!пидоры' and event.chat_id == 1:
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
                                dism[line[:-1:]] += 1
                            else:
                                dism[line[:-1:]] = 1
                        pidors.close()
                        #print(dism)
                        for i in spisok_chata:
                            if str(i) not in dism:
                                dism[i]=0
                        pidors_1 = []
                        smile={"1":"𝟭","2":"𝟮","3":"𝟯","4":"𝟰","5":"𝟱","6":"𝟲","7":"𝟳","8":"𝟴","9":"𝟵","0":"𝟬"}
                        print(dism)
                        for i in dism:
<<<<<<< HEAD
			    if i == '':
=======
                            if i == '':
>>>>>>> 668a16b0333c17bfc24b99882dacd16d8ddd66cd
                                continue
                            number_1 = ''
                            for k in str(dism[i]):
                                number_1 += smile[k]
                            #print(spisok_chata[int(i)])
                            pidors_1.append(spisok_chata[int(i)]+': ' + number_1 + ' раз(а)\n')
                        pidors_1 = ''.join(pidors_1)
                        #print(pidors_1)

                        vk.messages.send(
                            chat_id=1,
                            random_id=get_random_id(),
                            message=pidors_1
                        )

                    elif event.obj.text == '!гороскоп' or event.obj.text == 'гороскоп' and flkv == True or event.obj.text == 'гороскоп' and flkv2 == True:
                        if flagbddate==True:
                            bd_date = bd_date.split('.')
                            zodiak = goroscop(bd_date)
                            f=open('resurses/goroskop_files/'+zodiak+'.txt','r')
                            goroskp=f.read()
                            f.close()
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=goroskp
                            )
                        else:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message='У тебя нет даты Рождения ВК'
                            )

                    elif event.obj.text == '!анекдот' or event.obj.text == 'анекдот' and flkv == True or event.obj.text == 'анекдот' and flkv2 == True:
                        anes = random.randint(0, 135500)
                        print('попал в анекдот')
                        for linenum, line in enumerate(open('resurses/anec.txt', 'r')):
                            if linenum == anes:
                                anecdot = (line.strip()).replace('#', '\n')
                        print(anecdot)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=anecdot
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

                    elif event.obj.text.find('!погода на завтра в городе') != -1:
                        tommor = str(datetime.date.today()).split('-')
                        tommor[-1]=str(int(tommor[-1])+1)
                        tommor='-'.join(tommor)
                        city = event.obj.text[27::]+'/'+tommor
                        result = wheather(city,0,0)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('!погода на завтра') != -1:
                        try:
                            tommor = str(datetime.date.today()).split('-')
                            tommor[-1] = str(int(tommor[-1]) + 1)
                            tommor = '-'.join(tommor)
                            city = fio.text[14::].split(',')[7].split(':')[1][1:-5:].lower()+'/'+tommor
                        except:
                            city = "москва"
                            vk.messages.send(  # Отправляем собщение
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                            )
                        result = wheather(city,0,0)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('!погода в городе') != -1:
                        city = event.obj.text[17::]
                        print(city)
                        result = wheather(city,0,0)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message=result
                        )

                    elif event.obj.text.find('!погода') != -1 or event.obj.text.find(
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
                        result = wheather(city,0,0)
                        vk.messages.send(  # Отправляем собщение
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
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
