#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -

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

def sent_message_chat(text, chat_id, keyboard):
    vk.messages.send(
        chat_id=chat_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=text
    )
def sent_message_ls(text, user_id, keyboard):
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=text
    )

def vubor_slova():
    cit = random.randint(0, 402)
    for linenum, line in enumerate(open("/root/bot_herobot_chat/resurses/crocodile_files/crocodile_hard1.txt", mode="r")):
        if linenum == cit:
            messagecit = (line.strip())
    messagecit = messagecit.split("***")
    sent_message_ls("Твоё слово: " + messagecit[0].capitalize(), vedus_id, keyboardcet.get_keyboard())
    return [messagecit[1],messagecit[0]]


f=open("resurses/crocodile_files/crocodile_hard.txt",mode="r")
f1=open("resurses/crocodile_files/crocodile_hard1.txt",mode="w", encoding="utf-8")
print(f.encoding)
print(f1.encoding)
k=0
for line in f:
    k+=1
    f1.write(line)
    #print(line.split("***"))
print(k)
f.close()
f1.close()

#пустая клавиатура keyboard=keyboard1.get_empty_keyboard()

vedus_id = ""
slovo_zagadano = False
id_chat = ""
slovo = ""
winner_id = ""
slovo_ugadano = False
igra_okonchena = False
igra_nachata = False

'''
f=open("resurses/crocodile_files/stat.txt", mode="w", encoding="utf-8")
print(f.encoding)
f.close()
'''

keyboardemh = VkKeyboard(one_time=False, inline=True)

keyboardcet = VkKeyboard(one_time=False, inline=True)
keyboardcet.add_button('Что это такое?', color=VkKeyboardColor.PRIMARY)
keyboardcet.add_line()
keyboardcet.add_button('Другое слово', color=VkKeyboardColor.NEGATIVE)

keyboardcroc = VkKeyboard(one_time=False, inline=True)
keyboardcroc.add_button('Стать ведущим', color=VkKeyboardColor.PRIMARY)

for event in longpoll.listen():

    if slovo_zagadano is True and time.time() - time_start > 300:
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
            event.obj.from_id) + "&fields=bdate, city&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
        first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
        last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]

        if event.obj.text[:26:] == '[club178949259|ботхеработ]':
            event.obj.text = event.obj.text[27::]


        if event.obj.text[:30:] == '[club178949259|@club178949259]':
            event.obj.text = event.obj.text[31::]

        text = ''

        for h in event.obj.text:
            if h == "ё":
                text += "e"
            else:
                text += h

        if event.obj.text == '!крокодил' or event.obj.text == '! крокодил':
            if (id_chat == "" or id_chat == event.chat_id):
                if vedus_id == "":
                    sent_message_chat("Игра крокодил! (beta)", event.chat_id, keyboardcroc.get_keyboard())
                    id_chat = event.chat_id
                    igra_okonchena = False

                    igra_nachata = True
                    time_start_croc = time.time()

                else:
                    sent_message_chat("Игра уже идет!", event.chat_id, keyboardcroc.get_empty_keyboard())

            else:
                sent_message_chat("В данный момент игра невозможна, идет игра в другом чате!", event.chat_id, keyboardcroc.get_empty_keyboard())

        #print(event.obj.text)

        if event.obj.text == "стать ведущим" and winner_id == "":
            if id_chat == event.chat_id:
                if vedus_id == "":
                    igra_nachata = False
                    igra_okonchena = False
                    vedus_id = str(event.obj.from_id)

                    mass = vubor_slova()
                    opisanie, slovo = mass[0], mass[1]
                    slovo_zagadano = True
                    time_start = time.time()

                    #!!!sent_message_ls("Твоё слово: ", vedus_id, keyboardemh.get_keyboard())
                    sent_message_chat("Ведущий выбран, это " + first_name+' '+last_name+" , у него есть 5 минут на объяснение!", event.chat_id, keyboardcroc.get_empty_keyboard())
                else:
                    sent_message_chat("Ведущий уже выбран!", event.chat_id, keyboardcroc.get_empty_keyboard())
            else:
                sent_message_chat("Для начала игры пиши !крокодил",event.chat_id, keyboardcroc.get_empty_keyboard())

        elif event.obj.text == "стать ведущим" and winner_id == str(event.obj.from_id):
            if id_chat == event.chat_id:
                igra_okonchena = False
                igra_nachata = False
                vedus_id = str(event.obj.from_id)
                sent_message_chat(
                    first_name + ' ' + last_name + " воспользовался правом стать ведущим, у него есть 5 минут на объяснение!",
                    event.chat_id, keyboardcroc.get_empty_keyboard())

                mass = vubor_slova()
                opisanie, slovo = mass[0], mass[1]
                slovo_zagadano = True
                time_start = time.time()

            else:
                sent_message_chat("Для начала игры пиши !крокодил",event.chat_id, keyboardcroc.get_empty_keyboard())

        elif slovo_zagadano is True and id_chat == event.chat_id:
            if input_text == slovo: #and str(event.obj.from_id) != vedus_id:
                if str(event.obj.from_id) != vedus_id:
                    sent_message_chat("Слово угадано игроком " + first_name + ' ' + last_name + "!", event.chat_id, keyboardcroc.get_empty_keyboard())

                    winner_id = str(event.obj.from_id)
                    vedus_id = ""
                    slovo_zagadano = False
                    slovo = ""

                    f1 = open('/root/bot_herobot_chat/resurses/crocodile_files/stat.txt', 'a') #/root/bot_herobot_chat/
                    f1.write(str(winner_id) + '\n')
                    f1.close()

                    sent_message_chat("У угадавшего есть 30 секунд, чтобы стать ведущим!", event.chat_id, keyboardcroc.get_keyboard())

                    slovo_ugadano = True
                    igra_okonchena = True
                    time_end = time.time()
                else:
                    sent_message_chat(first_name + ' ' + last_name + ", вам защитано нарушение правил игры!",
                                      event.chat_id, keyboardcroc.get_empty_keyboard())

        elif (event.obj.text == '!рестарт крокодил' or event.obj.text == '! рестарт крокодил') and event.obj.from_id == 195310233:
            sent_message_chat("Крокодил сброшен!", event.chat_id, keyboardcet.get_empty_keyboard())

            vedus_id = ""
            slovo_zagadano = False
            id_chat = ""
            slovo = ""
            winner_id = ""
            slovo_ugadano = False
            igra_okonchena = False
            igra_nachata = False

    #часть работы в личных сообщениях
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_user and event.obj.from_id != -183679552:
        input_text = event.obj.text
        event.obj.text = event.obj.text.lower()

        if str(event.obj.peer_id) == vedus_id and event.obj.text == "другое слово":

            mass = vubor_slova()
            opisanie,slovo=mass[0],mass[1]
            slovo_zagadano = True
            time_start = time.time()

        elif str(event.obj.peer_id) == vedus_id and event.obj.text == "что это такое?":
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


