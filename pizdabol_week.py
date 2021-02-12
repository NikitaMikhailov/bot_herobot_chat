#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/bin/sh -

from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api import VkUpload
import requests
import vk_api
import time
import bot_functions
import bot_variable

if bot_variable.flag_repository:
    start_path = ""
else:
    start_path = '/root/bot_herobot_chat/'

if bot_variable.flag_smile:
    smile = bot_variable.smile_1
else:
    smile = bot_variable.smile_2

f = open('{}token.txt'.format(start_path), 'r')
token = f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

file_stat = open('{}logs_chat.txt'.format(start_path), 'r', encoding="utf-8")
sl = {}
for line in file_stat:
    line_1 = line
    line = line.split('*_*')
    if len(line) > 1 and line[3] == ' 1 ':
        number_words_in_message = 0
        for i in line[4].split(' '):
            if i != " " and i != "\n" and i != "":
                number_words_in_message += 1
        if line[2][1:-1] not in sl:
            last_people = line[2][1:-1]
            sl[line[2][1:-1]] = number_words_in_message
        else:
            last_people = line[2][1:-1]
            sl[line[2][1:-1]] += number_words_in_message
    elif len(line) == 1 and line != "\n":
        number_words_in_message = 0
        for i in line_1.split(' '):
            if i != " " and i != "\n" and i != "":
                number_words_in_message += 1
        sl[last_people] += number_words_in_message
file_stat.close()

file_word_in_week = open('{}word_in_week.txt'.format(start_path), 'r', encoding='utf-8')
sl_1 = {}
for line in file_word_in_week:
    sl_1[line.split('*_*')[0]] = int(line.split('*_*')[1][:-1:])
file_word_in_week.close()

week_result = {}
for i in sl:
    week_result[i] = int(sl[i]) - int(sl_1[i])

file_word_in_week = open('word_in_week.txt'.format(start_path), 'w', encoding='utf-8')
for i in sl:
    file_word_in_week.write(i+'*_*'+str(sl[i])+'\n')
file_word_in_week.close()

stats = []
kolp = []
for i in week_result:
    kolp.append(week_result[i])
kolp.sort()
kolp.reverse()
jstr = []
for i in kolp:
    for j in week_result:
        if j == '' or j == '\n':
            continue
        if str(week_result[j]) == str(i) and j not in jstr:
            jstr.append(j)
            number_2 = ''
            for k in str(week_result[j]):
                number_2 += smile[k]
            fio_1 = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(j)
                                 + "&fields=bdate&access_token=" + token + "&v=5.92").json()
            first_name_1 = fio_1["response"][0]["first_name"]
            last_name_1 = fio_1["response"][0]["last_name"]
            stats.append(first_name_1 + ' ' + last_name_1 + ': ' + str(
                number_2) + ' слов(а).\n')
for i in range(0, len(stats)):
    stats[i] = str(i + 1) + ") " + stats[i]
pizdabol = stats[0][stats[0].index(' ')+1:stats[0].index(':'):]
stats = ''.join(stats)
stats = "🔝 ТОП слов в беседе за прошедшую неделю:\n\n" + stats

for i in bot_variable.spisok_chata:
    if bot_variable.spisok_chata[i] == pizdabol:
        pizdabol_id = i

vk.messages.send(
    user_id=195310233,
    random_id=get_random_id(),
    message='Пиздабол недели обновлен в фоновом режиме, это [id' + str(pizdabol_id) + '|' + pizdabol + "]"
)


attachments = []
image_url = 'https://sun9-47.userapi.com/XOoZN_1DA7BZKe_QiWyPiKvCriZUFNKltkOe1A/nYo9ZMZUegw.jpg'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))


vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    attachment=','.join(attachments),
    message='Пиздабол недели [id' + str(pizdabol_id) + '|' + pizdabol + "]"+"!"
)
time.sleep(5)
vk.messages.send(
    chat_id=1,
    random_id=get_random_id(),
    message=stats
)