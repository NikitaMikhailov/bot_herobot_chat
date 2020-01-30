#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -

from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime, requests, vk_api, calendar, time
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

session = requests.Session()
vk_session = vk_api.VkApi(token='b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

def sent_message(text, chat_id, keyboard):
    vk.messages.send(
        chat_id=chat_id,
        random_id=get_random_id(),
        keyboard=keyboard,
        message=text
    )

#пустая клавиатура keyboard=keyboard1.get_empty_keyboard()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_chat and event.obj.from_id != -183679552:
        input_text = event.obj.text
        event.obj.text = event.obj.text.lower()
        if event.obj.text == '!крокодил' or event.obj.text == '! крокодил':
            keyboardcroc = VkKeyboard(one_time=False, inline=True)
            keyboardcroc.add_button('Стать ведущим', color=VkKeyboardColor.PRIMARY)
            sent_message("Тут будет игра крокодил!", event.chat_id, keyboardcroc.get_keyboard())


