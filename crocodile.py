#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -

from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api, time, random, json, wikipedia
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

#защита от пидарасов
f=open('/root/bot_herobot_chat/token.txt','r')
token=f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

#----------------------

kol_vo_slov = 3290+34010

#----------------------

def sent_message_chat(text, chat_id, keyboard):
    vk.messages.send(
        chat_id=chat_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=text
    )


def sent_message_ls(text, user_id, keyboard):
    message_ids = vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=text
    )
    return message_ids

def vubor_slova():
    cit = random.randint(0, kol_vo_slov - 1)
    for linenum, line in enumerate(open("resurses/crocodile_files/crocodile_hard1.txt",mode="r", encoding="utf-8")): #/root/bot_herobot_chat/resurses/
        if linenum == cit:
            messagecit = (line.strip())
    messagecit = messagecit.split("***")
    if len(messagecit) == 1:
        messagecit.append("Для данного слова нет описания 😔")
    sent_message_ls("Твоё слово: " + messagecit[0].title(), vedus_id, keyboardcet.get_keyboard())
    return [messagecit[1],messagecit[0]]


#пустая клавиатура keyboard=keyboard1.get_empty_keyboard()

vedus_id = ""
slovo_zagadano = False
id_chat = ""
slovo = ""
winner_id = ""
slovo_ugadano = False
igra_okonchena = False
igra_nachata = False

keyboardemh = VkKeyboard(one_time=False, inline=True)

keyboardcet = VkKeyboard(one_time=False, inline=True)
keyboardcet.add_button('❓ Что это такое', color=VkKeyboardColor.POSITIVE)
keyboardcet.add_line()
keyboardcet.add_button('♻ Другое слово', color=VkKeyboardColor.NEGATIVE)

keyboardcroc = VkKeyboard(one_time=False, inline=True)
keyboardcroc.add_button('🤵 Стать ведущим', color=VkKeyboardColor.PRIMARY)

keyboard1 = VkKeyboard(one_time=False)
keyboard1.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard1.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard1.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)

for event in longpoll.listen():

    if slovo_zagadano is True and time.time() - time_start > 900:
        sent_message_chat("Ведущий не успел объяснить слово, игра окончена!", event.chat_id,
                          keyboardcroc.get_keyboard())
        vedus_id = ""
        slovo_zagadano = False
        slovo = ""
        id_chat = ""

    if slovo_ugadano is True and time.time() - time_end > 30:
        slovo_ugadano = False
        winner_id = ""

    if igra_okonchena is True and time.time() - time_end > 300:
        if event.chat_id == id_chat:
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboard1.get_keyboard(),
                message="Ведущий не выбран в отведенное время, игра окончена!"
            )
            id_chat = ""
            igra_okonchena = False
        else:
            id_chat = ""
            igra_okonchena = False

    if igra_nachata is True and time.time() - time_start_croc > 300:
        if event.chat_id == id_chat:
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboard1.get_keyboard(),
                message="Ведущий не выбран в отведенное время, игра окончена!"
            )
            id_chat = ""
            igra_nachata = False
        else:
            id_chat = ""
            igra_nachata = False

    #часть работы в чате
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_chat and event.obj.from_id != -183679552:
        input_text = event.obj.text.lower()
        event.obj.text = event.obj.text.lower()

        fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
            event.obj.from_id) + "&fields=bdate, city, can_write_private_message&access_token="+token+"&v=5.92")
        first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
        last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]

        if event.obj.text[:26:] == '[club178949259|ботхеработ]':
            event.obj.text = event.obj.text[27::]

        if event.obj.text[:30:] == '[club178949259|@club178949259]':
            event.obj.text = event.obj.text[31::]

        text = ''

        for h in event.obj.text:
            if h == "ё":
                text += "е"
            else:
                text += h
        event.obj.text = text
        input_text = text

        text = ""
        for h in event.obj.text:
            if h == "-":
                text += " "
            else:
                text += h

        event.obj.text = text
        input_text = text

        if (event.obj.text == '!рестарт крокодил' or event.obj.text == '! рестарт крокодил') and event.obj.from_id == 195310233:
            if igra_nachata is True:
                sent_message_chat("Крокодил сброшен!", event.chat_id, keyboard1.get_empty_keyboard())
                sent_message_chat("🐊 Игра крокодил! (beta)", event.chat_id, keyboardcroc.get_keyboard())

                vedus_id = ""
                slovo_zagadano = False
                id_chat = ""
                slovo = ""
                winner_id = ""
                slovo_ugadano = False

                id_chat = event.chat_id
            igra_okonchena = False
            igra_nachata = True
            time_start_croc = time.time()


        if event.obj.text == '!крокодил' or event.obj.text == '! крокодил':
            if (id_chat == "" or id_chat == event.chat_id):
                if vedus_id == "":
                    sent_message_chat("🐊 Игра крокодил! (beta)", event.chat_id, keyboardcroc.get_keyboard())
                    rt = requests.get('https://api.vk.com/method/messages.getConversationMembers?peer_id=200000000'+
                                      str(event.chat_id) +'&fields=count,items,profiles1&access_token='+token+'&v=5.92')
                    zapros = json.loads(rt.text)
                    spisok_uchastnikov = []
                    for i in (zapros["response"]['profiles']):
                        spisok_uchastnikov.append("[id"+str(i['id'])+'|&#8203;]')
                    #print(''.join(spisok_uchastnikov))
                    sent_message_chat("Началась игра крокодил!"+''.join(spisok_uchastnikov), event.chat_id, keyboardcroc.get_empty_keyboard())
                    id_chat = event.chat_id
                    igra_okonchena = False

                    igra_nachata = True
                    time_start_croc = time.time()

                else:
                    sent_message_chat("Игра уже идет!", event.chat_id, keyboardcroc.get_empty_keyboard())

            else:
                sent_message_chat("В данный момент игра невозможна, идет игра в другом чате!", event.chat_id, keyboardcroc.get_empty_keyboard())

        #print(event.obj.text)

        if event.obj.text == "🤵 стать ведущим" and winner_id == "":
            if id_chat == event.chat_id:
                if vedus_id == "":
                    try:
                        igra_nachata = False
                        igra_okonchena = False
                        vedus_id = str(event.obj.from_id)

                        mass = vubor_slova()
                        opisanie, slovo = mass[0], mass[1]
                        slovo_zagadano = True
                        time_start = time.time()

                        sent_message_chat("Ведущий выбран, это " + first_name+' '+last_name+" , у него есть 15 минут на объяснение!",
                                          event.chat_id, keyboardcroc.get_empty_keyboard())
                    except:
                        sent_message_chat("Чтобы стать ведущим нужно открыть доступ к личным сообщениям для бота!",
                                          event.chat_id, keyboardcet.get_empty_keyboard())
                        time_end = time.time() - 30
                        igra_okonchena = True
                        vedus_id = ""
                else:
                    sent_message_chat("Ведущий уже выбран!", event.chat_id, keyboardcroc.get_empty_keyboard())
            else:
                sent_message_chat("Для начала игры пиши !крокодил",event.chat_id, keyboardcroc.get_empty_keyboard())

        elif event.obj.text == "🤵 стать ведущим" and winner_id == str(event.obj.from_id):
            if id_chat == event.chat_id:
                try:
                    igra_okonchena = False
                    igra_nachata = False
                    vedus_id = str(event.obj.from_id)
                    mass = vubor_slova()
                    sent_message_chat(
                        first_name + ' ' + last_name + " воспользовался правом стать ведущим, у него есть 15 минут на объяснение!",
                        event.chat_id, keyboardcroc.get_empty_keyboard())
                    opisanie, slovo = mass[0], mass[1]
                    slovo_zagadano = True
                    time_start = time.time()
                except:
                    sent_message_chat("Чтобы стать ведущим нужно открыть доступ к личным сообщениям для бота!",
                                      event.chat_id, keyboardcet.get_empty_keyboard())
                    time_end = time.time() - 30
                    igra_okonchena = True
                    vedus_id = ""

            else:
                sent_message_chat("Для начала игры пиши !крокодил",event.chat_id, keyboardcroc.get_empty_keyboard())

        elif slovo_zagadano is True and id_chat == event.chat_id:
            if str(input_text) == str(slovo): #and str(event.obj.from_id) != vedus_id:
                if str(event.obj.from_id) != vedus_id:
                    sent_message_chat("Слово угадано игроком " + first_name + ' ' + last_name + "!", event.chat_id, keyboardcroc.get_empty_keyboard())

                    winner_id = str(event.obj.from_id)
                    vedus_id = ""
                    slovo_zagadano = False
                    slovo = ""

                    f1 = open('resurses/crocodile_files/stat.txt', 'a') #/root/bot_herobot_chat/
                    f1.write(str(winner_id) + '***' +str(event.chat_id) +'\n')
                    f1.close()

                    sent_message_chat("У угадавшего есть 30 секунд, чтобы стать ведущим!", event.chat_id, keyboardcroc.get_keyboard())

                    slovo_ugadano = True
                    igra_okonchena = True
                    time_end = time.time()
                    try:
                        message_id=sent_message_ls("&#8203;",int(winner_id),keyboardcroc.get_empty_keyboard())
                        rt = requests.get('https://api.vk.com/method/messages.delete?message_ids=' + str(
                            message_id) + '&delete_for_all=1&access_token='+token+'&v=5.92')
                    except:
                        time_end = time.time()-30
                else:

                    f1 = open('resurses/crocodile_files/stat.txt','r')  # /root/bot_herobot_chat/
                    flag_udalil_ochko = False
                    spisok_pobed = []
                    for line in f1:
                        if line == str(event.obj.from_id)+"***"+str(event.chat_id)+"\n" and flag_udalil_ochko is False:
                            flag_udalil_ochko = True
                            continue
                        else:
                            spisok_pobed.append(line)
                    f1.close()
                    f1 = open('resurses/crocodile_files/stat.txt','w')  # /root/bot_herobot_chat/
                    f1.write(''.join(spisok_pobed))
                    f1.close()

                    sent_message_chat(first_name + ' ' + last_name + ", вам защитано нарушение правил игры, у вас стало на одно угаданное слово меньше!",
                                      event.chat_id, keyboardcroc.get_empty_keyboard())

    #часть работы в личных сообщениях
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_user and event.obj.from_id != -183679552:
        input_text = event.obj.text
        event.obj.text = event.obj.text.lower()

        if str(event.obj.peer_id) == vedus_id and event.obj.text == "♻ другое слово":

            mass = vubor_slova()
            opisanie,slovo=mass[0],mass[1]
            slovo_zagadano = True
            time_start = time.time()

        elif str(event.obj.peer_id) == vedus_id and event.obj.text == "❓ что это такое":
            wikipedia.set_lang("ru")
            try:
                opisanie = wikipedia.summary(slovo).split("\n")[0]
                '''
                try:
                    g = wikipedia.page(slovo)
                    opisanie = g.content.split('\n')[0]
                except wikipedia.exceptions.DisambiguationError as e:
                    k = e.options
                    g = wikipedia.page(k[1])
                    opisanie = g.content.split('\n')[0]
                '''
            except:
                opisanie = "Для данного слова нет описания 😔"
            sent_message_ls(opisanie, vedus_id, keyboardcet.get_empty_keyboard())

        elif (event.obj.text == '!рестарт крокодил' or event.obj.text == '! рестарт крокодил') and event.obj.from_id == 195310233:
            sent_message_ls("Крокодил сброшен!", 195310233, keyboardcet.get_empty_keyboard())

            vedus_id = ""
            slovo_zagadano = False
            id_chat = ""
            slovo = ""
            winner_id = ""
            slovo_ugadano = False
            igra_okonchena = False
            igra_nachata = False


