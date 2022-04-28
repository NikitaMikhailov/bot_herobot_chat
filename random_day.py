#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -

from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api import VkUpload
import random
import requests
import vk_api
import time
import bot_functions
import bot_variable

chat_id = "1"

if bot_variable.flag_repository:
    start_path = ""
else:
    start_path = '/root/bot_herobot_chat/'

f = open('{}token.txt'.format(start_path), 'r')
token = f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)


def send_block(pidor_id, pidor):
    vk.messages.send(
        user_id=bot_variable.my_id,
        random_id=get_random_id(),
        message='Пидор дня обновлен в фоновом режиме, это [id' + str(pidor_id) + '|' + pidor + "]"
    )

    attachments = []
    image_url = 'https://pp.userapi.com/c621701/v621701407/73af/RYLX4AO4K7s.jpg'
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

    vk.messages.send(
        chat_id=chat_id,
        random_id=get_random_id(),
        attachment=','.join(attachments),
        message="Так-так-так, у нас ежедневная рубрика!"
    )
    time.sleep(10)
    vk.messages.send(
        chat_id=chat_id,
        random_id=get_random_id(),
        message="Вот это неожиданность, оказывается, что ..."
    )
    time.sleep(10)
    vk.messages.send(
        chat_id=chat_id,
        random_id=get_random_id(),
        message="[id" + str(pidor_id) + '|' + pidor + "] Ты пидор дня."
    )


def main():
    # получим список участников чата
    pidor_info = random.choice(bot_functions.dialog_users_list(chat_id)[1])
    pidor_id = pidor_info.split(" ")[0]
    pidor = " ".join(pidor_info.split(" ")[1::])

    print(pidor, pidor_id)

    f1 = open('{}resurses/pidors.txt'.format(start_path), 'a')
    f1.write(str(pidor_id) + '\n')
    f1.close()

    f1 = open('{}resurses/pidor_today.txt'.format(start_path), 'w')
    f1.write(str(pidor) + " --- " + str(pidor_id))
    f1.close()

    send_block(pidor_id, pidor)


if __name__ == "__main__":
    main()
