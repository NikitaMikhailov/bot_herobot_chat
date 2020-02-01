#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -

from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime, requests, vk_api, calendar, time, random
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

def vubor_slova(level):
    cit = random.randint(0, 99)
    for linenum, line in enumerate(open("resurses/crocodile_files/crocodile_"+level+".txt", mode="r")):
        if linenum == cit:
            messagecit = (line.strip())
    messagecit = messagecit.split("***")
    sent_message_ls(messagecit[0].capitalize(), vedus_id, keyboardcet.get_keyboard())
    return [messagecit[1]]


'''
f=open("resurses/crocodile_files/crocodile_hard.txt",mode="r")
k=0
for line in f:
    k+=1
    print(line.split("***"))
print(k)
'''
#пустая клавиатура keyboard=keyboard1.get_empty_keyboard()

vedus_id = ""
slovo_zagadano = False
id_chat = ""


keyboardemh = VkKeyboard(one_time=False, inline=True)
keyboardemh.add_button('Легкое', color=VkKeyboardColor.POSITIVE)
keyboardemh.add_button('Среднее', color=VkKeyboardColor.PRIMARY)
keyboardemh.add_button('Сложное', color=VkKeyboardColor.NEGATIVE)

keyboardcet = VkKeyboard(one_time=False, inline=True)
keyboardcet.add_button('Что это такое?', color=VkKeyboardColor.PRIMARY)

keyboardcroc = VkKeyboard(one_time=False, inline=True)
keyboardcroc.add_button('Стать ведущим', color=VkKeyboardColor.PRIMARY)

for event in longpoll.listen():
    #часть работы в чате
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_chat and event.obj.from_id != -183679552:
        input_text = event.obj.text
        event.obj.text = event.obj.text.lower()

        fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
            event.obj.from_id) + "&fields=bdate, city&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92")
        first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
        last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]

        if event.obj.text[:26:] == '[club178949259|ботхеработ]':
            event.obj.text = event.obj.text[27::]


        if event.obj.text[:30:] == '[club178949259|@club178949259]':
            event.obj.text = event.obj.text[31::]


        if event.obj.text == '!крокодил' or event.obj.text == '! крокодил':
            if id_chat == "":
                sent_message_chat("Тут будет игра крокодил!", event.chat_id, keyboardcroc.get_keyboard())
                id_chat = event.chat_id
            else:
                sent_message_chat("В данный момент игра невозможна, идет игра в другом чате!", event.chat_id, keyboardcroc.get_empty_keyboard())

        #print(event.obj.text)

        if event.obj.text == "стать ведущим" and vedus_id == "":
            if id_chat == event.chat_id:
                vedus_id = str(event.obj.from_id)

                sent_message_ls("Выбери сложность слова", vedus_id, keyboardemh.get_keyboard())
                sent_message_chat("Ведущий выбран, это " + '[id' + str(vedus_id) + '|' + first_name+' '+last_name + "]", event.chat_id, keyboardcroc.get_empty_keyboard())
            else:
                sent_message_chat("Для начала игры пиши !крокодил",event.chat_id, keyboardcroc.get_empty_keyboard())

        elif event.obj.text == "стать ведущим" and vedus_id == str(event.obj.from_id):
            if id_chat == event.chat_id:
                vedus_id = str(event.obj.from_id)

                sent_message_ls("Выбери сложность слова", vedus_id, keyboardemh.get_keyboard())
            else:
                sent_message_chat("Для начала игры пиши !крокодил",event.chat_id, keyboardcroc.get_empty_keyboard())

    #часть работы в личных сообщениях
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_user and event.obj.from_id != -183679552:
        input_text = event.obj.text
        event.obj.text = event.obj.text.lower()

        if str(event.obj.peer_id) == vedus_id and event.obj.text == "легкое":
            if slovo_zagadano is False:
                opisanie=vubor_slova("easy")[0]
                slovo_zagadano = True
                sent_message_chat("Ведущему загадано слово, у него есть 5 минут на объяснение!", id_chat,
                                  keyboardcroc.get_empty_keyboard())

                time_start = time.time()

            else:
                sent_message_ls("Слово уже загадано!", vedus_id, keyboardcet.get_empty_keyboard())

        elif str(event.obj.peer_id) == vedus_id and event.obj.text == "среднее":
            if slovo_zagadano is False:
                opisanie=vubor_slova("middle")[0]
                slovo_zagadano = True
                sent_message_chat("Ведущему загадано слово, у него есть 5 минут на объяснение!", id_chat,
                                  keyboardcroc.get_empty_keyboard())

                time_start = time.time()

            else:
                sent_message_ls("Слово уже загадано!", vedus_id, keyboardcet.get_empty_keyboard())

        elif str(event.obj.peer_id) == vedus_id and event.obj.text == "сложное":
            if slovo_zagadano is False:
                opisanie=vubor_slova("hard")[0]
                slovo_zagadano = True
                sent_message_chat("Ведущему загадано слово, у него есть 5 минут на объяснение!", id_chat,
                                  keyboardcroc.get_empty_keyboard())

                time_start = time.time()

            else:
                sent_message_ls("Слово уже загадано!", vedus_id, keyboardcet.get_empty_keyboard())

        elif str(event.obj.peer_id) == vedus_id and event.obj.text == "что это такое?":
            sent_message_ls(opisanie, vedus_id, keyboardcet.get_empty_keyboard())

    if slovo_zagadano is True and time.time()-time_start > 300:
        sent_message_chat("Ведущий не успел объяснить слово, игра окончена!", event.chat_id, keyboardcroc.get_keyboard())
        vedus_id = ""
        slovo_zagadano = False
        id_chat = ""
