#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -

import random
import time

import requests
import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

import bot_functions
import bot_variable

# -------------------------------------------------------------
keyboard1 = VkKeyboard(one_time=False)
keyboard1.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard1.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard1.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
# -------------------------------------------------------------
keyboard2 = VkKeyboard(one_time=False)
keyboard2.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboard2.add_button('Факт', color=VkKeyboardColor.PRIMARY)
# -------------------------------------------------------------
keyboard3 = VkKeyboard(one_time=False)
keyboard3.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Погода', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Гороскоп', color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
keyboard3.add_button('Факт', color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button('Отстань', color=VkKeyboardColor.NEGATIVE)
keyboard3.add_button('Вернись', color=VkKeyboardColor.POSITIVE)
# -------------------------------------------------------------

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

if bot_variable.flag_hello_message:
    hello_message = ""
    for i in range(1, 10):
        vk.messages.send(
            chat_id=i,
            random_id=get_random_id(),
            keyboard=bot_variable.keyboard1.get_keyboard(),
            message=hello_message
        )


def main(event):
    # эти флаги отвечают за работу со стопом активности бота
    global like_you, messagecit, anecdot, last_people, flag_eat_2
    flagtime = False
    fltm1 = False
    fltm2 = False

    attachments = []

    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text and event.from_chat and event.obj.from_id > 0:

        flkv, flkv2, text_message = bot_functions.text_transform(event.obj.text)

        city, flag_city, first_name, last_name, bd_date, flagbddate = bot_functions.requests_fio_city_bddate(event)

        # запись сообщения в лог файл

        s = open('logs_chat.txt', 'a', encoding="utf-8")
        s.write(last_name + ' *_* ' + first_name + ' *_* ' + str(event.obj.from_id) + ' *_* ' + str(
            event.chat_id) + ' *_* ' + text_message + '\n')
        s.close()

        # проверка на поздравление с др и поздравление

        pozdrflag = False
        pozdr = open('resurses/pozdravlenie.txt', 'r')
        for i in pozdr:
            if str(event.obj.from_id) == i[:-1:]:
                pozdrflag = True
        pozdr.close()
        if flagbddate and str(bot_variable.dict_month[time.strftime("%B", time.localtime())]) == bd_date.split('.')[1] \
                and bot_functions.today_without_zero() == bd_date.split('.')[0] and pozdrflag is False:
            pozdr = open('resurses/pozdravlenie.txt', 'a')
            pozdr.write(str(event.obj.from_id) + '\n')
            pozdr.close()
            image_url = 'https://pp.userapi.com/c850128/v850128497/10e229/uPpRrYrMR-4.jpg'
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                attachment=','.join(attachments),
                message="О, " + first_name + ", Поздравляю тебя с Днём Рождения! 💐💐💐\n\
                        Моё железное сердце всегда радуется твоим сообщениям!"
            )

        # флаг на обращение к конкретному пользователю, бот игнорирует, если True

        flagobr = False
        for i in range(len(bot_variable.list_name)):
            if text_message.find(bot_variable.list_name[i]) != -1:
                flagobr = True

        # флаг на обращение к пидору

        flagobrpidor = False
        for i in text_message.split(" "):
            if i == "пидор":
                flagobrpidor = True

        # флаг на триггер к картинке "пить"

        flag_eat = False
        event1 = text_message.split(' ')
        for word_eat in event1:
            if word_eat in bot_variable.list_eat:
                if word_eat != 'есть':
                    flag_eat = True
                    flag_eat_2 = word_eat
                    break
                elif word_eat == 'есть':
                    for word_going in bot_variable.list_going:
                        if text_message.find(word_going) != -1:
                            flag_eat = True
                            flag_eat_2 = word_going + " " + word_eat
                            break
                    break

        # флаг на матные  слова в тексте сообщения, подсчет их количества

        flag_swearing = False
        kol_mat_in_text = 0
        event1 = text_message.replace("\n", " ").split(' ')
        for word_in_message in event1:
            mat = open('resurses/matsp1.txt', mode='r')
            for k in mat:
                if str(word_in_message) == k[:-1:]:
                    flag_swearing = True
                    kol_mat_in_text += 1
            mat.close()

        # флаг на фразу "пиздуй учиться"

        flag_learning = False
        event1 = text_message.split(' ')
        for word_in_message in event1:
            word_in_message = str(word_in_message)
            if word_in_message in bot_variable.list_laziness:
                flag_learning = True

        # флаг на фразу "сам такой"

        flag_like_you = False
        event1 = text_message.split(' ')
        for i in bot_variable.list_like_you:
            for k in range(0, len(event1)):
                if event1[k] == i:
                    flag_like_you = True
                    like_you = i

        # обработка мата в сообщении

        if flag_swearing and text_message.replace(" ", "").find('!отъебись') == -1 \
                and text_message.replace(" ", "").find('!пидоры') == -1 \
                and text_message.replace(" ", "").find('!пидордня') == -1:
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
                    message='Теперь у тебя {} грязных словечек в чате, я всё вижу, {}.'.format(str(chmat), first_name)
                )
                f1.close()
            except vk_api.exceptions.VkApiError:
                vk.messages.send(
                    user_id=bot_variable.my_id,
                    random_id=get_random_id(),
                    message='Возникла ошибка в доступе к личным сообщениям, id пользователя {} имя пользователя {} {}.'. \
                        format(str(event.obj.from_id), first_name, last_name)
                )
                f1.close()

        # обработка команды помощи
        elif (text_message.replace(" ", "") == '!help'
              or text_message.replace(" ", "") == "!помощь"
              or text_message.replace(" ", "") == "!хелп"):
            if event.chat_id == 1:
                message_help = bot_variable.message_help_1
            else:
                message_help = bot_variable.message_help_2
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=message_help
            )

        # обработка клавиатур для чатов
        elif text_message.replace(" ", "").replace("1", "") == '!клавиатуравкл':
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboard1.get_keyboard(),
                message='Клавиатура тип 1 включена.'
            )
        elif text_message.replace(" ", "") == '!клавиатура2вкл':
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboard2.get_keyboard(),
                message='Клавиатура тип 2 включена.'
            )
        elif text_message.replace(" ", "") == '!клавиатура3вкл':
            if event.chat_id == 1:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    keyboard=keyboard3.get_keyboard(),
                    message='Клавиатура тип 3 включена.'
                )
            else:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='Данный тип клавиатуры не доступен в этом чате.'
                )
        elif text_message.replace(" ", "") == '!клавиатуравыкл':
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboard1.get_empty_keyboard(),
                message='Клавиатура выключена'
            )

        # обработка однословных команд бота

        elif flag_like_you and not flagobr and not flagtime:
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Сам такой, ' + like_you + ', ' + last_name
            )

        elif text_message.replace(" ", "") == '!антон':
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                # attachment='audio195310233_456240687',
                message='Команда выведена из использования.'
            )

        elif text_message.replace(" ", "") == '!мысль' \
                or text_message == 'мысль' and (flkv or flkv2):
            cit = random.randint(0, 1355)
            for linenum, line in enumerate(open('resurses/quotes_clear.txt', 'r')):
                if linenum == cit:
                    messagecit = (line.strip())
            if messagecit[-1] == ',':
                messagecit = messagecit[:-1:]
            keyboardquotes = VkKeyboard(one_time=False, inline=True)
            keyboardquotes.add_button('Мысль', color=VkKeyboardColor.PRIMARY)
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboardquotes.get_keyboard(),
                message=str(messagecit)
            )

        elif text_message.replace(" ", "") == '!факт' \
                or text_message == 'факт' and (flkv or flkv2):
            cit = random.randint(0, 764)
            for linenum, line in enumerate(open('resurses/facts_clear.txt', 'r')):
                if linenum == cit:
                    messagecit = (line.strip())
            if messagecit[-1] == ',':
                messagecit = messagecit[:-1:]
            keyboardfacts = VkKeyboard(one_time=False, inline=True)
            keyboardfacts.add_button('Факт', color=VkKeyboardColor.PRIMARY)
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboardfacts.get_keyboard(),
                message=str(messagecit)
            )

        elif text_message.replace(" ", "") == '!цитата' \
                or text_message == 'цитата' and (flkv or flkv2):
            cit = random.randint(0, 1391)
            for linenum, line in enumerate(open('resurses/twtrr.txt', 'r')):
                if linenum == cit:
                    messagecit = (line.strip())
            if messagecit[-1] == ',':
                messagecit = messagecit[:-1:]
            keyboardtwtrr = VkKeyboard(one_time=False, inline=True)
            keyboardtwtrr.add_button('Цитата', color=VkKeyboardColor.PRIMARY)
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboardtwtrr.get_keyboard(),
                message=str(messagecit)
            )

        elif text_message.replace(" ", "") == '!анекдот' or text_message == 'анекдот' and (flkv or flkv2):
            anes = random.randint(0, 135500)
            for linenum, line in enumerate(open('resurses/anec.txt', 'r')):
                if linenum == anes:
                    anecdot = (line.strip()).replace('#', '\n')

            keyboardanec = VkKeyboard(one_time=False, inline=True)
            keyboardanec.add_button('Анекдот', color=VkKeyboardColor.PRIMARY)
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboardanec.get_keyboard(),
                message=anecdot
            )

        elif text_message.replace(" ", "") == '!обновигороскоп':
            if event.obj.from_id == bot_variable.my_id:
                bot_functions.goroscop_update()
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='Обновил.'
                )
            else:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='Вам недоступна данная команда.'
                )

        elif text_message.replace(" ", "") == '!стата' and (
                event.chat_id == 1 or event.chat_id == 5):
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

            stats = []
            kolp = []
            for i in sl:
                kolp.append(sl[i])
            kolp.sort()
            kolp.reverse()
            jstr = []
            for i in kolp:
                for j in sl:
                    if j == '' or j == '\n':
                        continue
                    if str(sl[j]) == str(i) and j not in jstr:
                        jstr.append(j)
                        number_2 = ''
                        for k in str(sl[j]):
                            number_2 += smile[k]

                        stats.append(bot_functions.name_about_id(str(j))[0] + ' ' +
                                     bot_functions.name_about_id(str(j))[1] + ': ' + str(number_2) + ' слов(а).\n')

            for i in range(0, len(stats)):
                stats[i] = str(i + 1) + ") " + stats[i]
            stats = ''.join(stats)
            stats = "🔝 ТОП слов в беседе:\n\n" + stats
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=stats
            )

        elif text_message.replace(" ", "") == '!крокодилстата':
            f = open('{}resurses/crocodile_files/stat.txt'.format(start_path), 'r')
            dism = {}
            for line in f:
                g = line.split("***")
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
                        mat.append(bot_functions.name_about_id(str(j))[0] + ' ' +
                                   bot_functions.name_about_id(str(j))[1] + ': ' + str(number_2) +
                                   ' раз(а) угадал слово.\n')
            for i in range(0, len(mat)):
                mat[i] = str(i + 1) + ") " + mat[i]
            mat = ''.join(mat)
            mat = "🔝 ТОП крокодила:\n\n" + mat
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=mat
            )

        elif text_message.replace(" ", "") == '!маты':
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

                        mat.append(bot_functions.name_about_id(j[:-1:])[0] + ' ' +
                                   bot_functions.name_about_id(j[:-1:])[1] + ': ' + str(number_2) + ' раз(а)\n')

            for i in range(0, len(mat)):
                mat[i] = str(i + 1) + ") " + mat[i]
            mat = ''.join(mat)
            mat = "🔝 ТОП мата:\n\n" + mat
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=mat
            )

        elif text_message.replace(" ", "") == '!пидордня' and (event.chat_id == 1 or event.chat_id == 5):
            f1 = open('resurses/pidor_today.txt', 'r')
            pidor_2 = f1.read()
            f1.close()
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message="Сегодня пидор дня " + pidor_2.split(" --- ")[0]
            )

        elif flagobrpidor and (event.chat_id == 1 or event.chat_id == 5):
            f1 = open('resurses/pidor_today.txt', 'r')
            pidor_2 = f1.read()
            f1.close()
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=("[id" + pidor_2.split(" --- ")[1]) + '|&#8203;]'
            )

        elif text_message.replace(" ", "") == '!пидоры' and (event.chat_id == 1 or event.chat_id == 5):
            pidors = open('resurses/pidors.txt', 'r')
            dism = {}
            for line in pidors:
                if line in dism:
                    dism[line] += 1
                else:
                    dism[line] = 1
            pidors.close()
            for i in bot_variable.spisok_chata:
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
                    if str(dism[j]) == str(i) and j not in jstr and bot_variable.spisok_chata[int(j)] not in nstr:
                        nstr.append(bot_variable.spisok_chata[int(j)])
                        jstr.append(j)
                        number_1 = ''
                        for k in str(dism[j]):
                            number_1 += smile[k]
                        pidors_1.append(bot_variable.spisok_chata[int(j)] + ': ' + number_1 + ' раз(а)\n')

            for i in range(0, len(pidors_1)):
                pidors_1[i] = str(i + 1) + ") " + pidors_1[i]
            pidors_1 = ''.join(pidors_1)
            pidors_1 = "🔝 ТОП пидоров дня:\n\n" + pidors_1

            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=pidors_1
            )
        elif text_message.replace(" ", "") == '!гороскоп' \
                or text_message == 'гороскоп' and (flkv or flkv2):
            if flagbddate:
                bd_date = bd_date.split('.')
                zodiak = bot_functions.goroscop_user(bd_date)
                f = open('resurses/goroskop_files/' + zodiak + '.txt', 'r')
                goroskp = f.read()
                f.close()
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message=bot_variable.simbol_zodiak[zodiak] + ' ' + goroskp
                )
            else:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='У тебя нет даты Рождения ВК'
                )


        elif flag_eat and not flagobr and not flagtime:
            image_url = 'https://pp.userapi.com/c851020/v851020736/cb17f/BgYwz2bShuc.jpg'
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id'])
                               )
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                attachment=','.join(attachments),
                message='Кто сказал ' + flag_eat_2 + '?'
            )

        elif text_message.find('!прогноз в городе') != -1 or text_message.find(
                '! прогноз в городе') != -1:
            if text_message.find('!прогноз в городе') != -1:
                inder = 18
            else:
                inder = 19

            city_1 = text_message[inder::]
            result = bot_functions.wheather_tomm(city_1)
            result = "Прогноз в городе " + city_1.capitalize().split('/')[0] + ':\n\n' + result
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=result
            )

        elif text_message.find('!прогноз') != -1 \
                or text_message.find('! прогноз') != -1 \
                or text_message.find('☂ прогноз') != -1 and (flkv or flkv2):

            if flag_city:
                city = str(city).lower()
            else:
                city = "москва"
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                )
            result = bot_functions.wheather_tomm(city)
            result = "Прогноз в городе " + city.capitalize().split('/')[0] + ':\n\n' + result
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=result
            )

        elif text_message.find('!погода в городе') != -1 or text_message.find('! погода в городе') != -1:
            if text_message.find('!погода в городе') != -1:
                inder = 17
            else:
                inder = 18
            city_1 = text_message[inder::]
            result = bot_functions.wheather_today(city_1)
            vk.messages.send(  # Отправляем собщение
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=result
            )

        elif text_message.replace(" ", "").find('!погода') != -1 \
                or text_message.find('погода') != -1 and flkv \
                or text_message.find('погода') != -1 and flkv2:
            if flag_city:
                city = str(city).lower()
            else:
                city = 'москва'
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message="У Вас не указан город ВК, по умолчанию выставлена Москва"
                )
            keyboardweather = VkKeyboard(one_time=False, inline=True)
            keyboardweather.add_button('☂ Прогноз', color=VkKeyboardColor.PRIMARY)
            result = bot_functions.wheather_today(city)
            vk.messages.send(  # Отправляем собщение
                chat_id=event.chat_id,
                random_id=get_random_id(),
                keyboard=keyboardweather.get_keyboard(),
                message=result
            )

        elif text_message.find('купи слона') != -1 or text_message.find('!купи слона') != -1:
            if text_message.find('!купи слона') != -1:
                text_message = "".join(text_message.split("!"))
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Все говорят {}, а ты купи слона'.format(text_message)
            )

        elif text_message.find('!кубик') != -1:
            kub = text_message[7::]
            try:
                vypalo = random.randint(1, int(kub))
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='Выпало число {}'.format(vypalo)
                )
            except ValueError:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    message='С твоим числом что-то не так..'
                )

        elif text_message == 'ну и ладно' and not flagtime:
            image_url = 'https://pp.userapi.com/c851120/v851120719/d26d3/-orcQNPA2gI.jpg'
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                attachment=','.join(attachments),
                message=''
            )

        elif text_message.split(' ')[-1] == "нет" and not flagtime:
            a = random.randint(0, 2)
            if random.randint(0, 1) == 1 and event.obj.from_id == 51556033:
                a = 2
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=bot_variable.list_answer_no[a]
            )

        elif not flagtime and (text_message[-3::] == "300" or text_message[-6::] == "триста"):
            a = random.randint(0, 4)
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message=bot_variable.list_answer_300[a]
            )

        elif not flagtime and (text_message.split(' ')[-1] == "бот" or text_message == '!бот'):
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Херабот!'
            )

        elif flag_learning and not flagtime:
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Пиздуй работать, ' + first_name + '!'
            )

        elif not flagtime and (text_message.split(' ')[-1] == "чо" or text_message.split(' ')[-1] == "че"
                               or text_message.split(' ')[-1] == "чё"):
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Перекинь через плечо!'
            )

        elif text_message.split(' ')[-1] == "да" and not flagtime:
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=get_random_id(),
                message='Сковорода!'
            )


if __name__ == "__main__":
    for event in longpoll.listen():
        main(event)

'''        
if __name__ == "__main__":
    try:
        for event in longpoll.listen():
            main(event)
    except Exception as err:
        vk.messages.send(
            user_id=bot_variable.my_id,
            random_id=get_random_id(),
            message='Возникла ошибка:\n{}\nв bot_herobot_chat.'.format(str(err))
        )
'''
