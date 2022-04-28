#!/usr/bin/env bash
# !/bin/bash
# !/bin/sh
# !/bin/sh -


import bs4
import requests
import bot_variable
import time

if bot_variable.flag_repository:
    start_path = ""
else:
    start_path = '/root/bot_herobot_chat/'

f = open('{}token.txt'.format(start_path), 'r')
token = f.read()
f.close()


# функция, выполняющая обновление файлов гороскопа


def goroscop_update():
    f_1 = open('{}token_2.txt'.format(start_path), 'r')
    token_1 = f_1.read()
    f_1.close()

    file_req = requests.get("https://api.vk.com/method/wall.get?owner_id=-193489972&domain=neural_horo&access_token=" +
                            token_1 + "&v=5.131&offset=1&count=1&filter=all").json()

    goroskop_text = (file_req['response']['items'][0]['text']).split('\n')
    goroskop_text_1 = []
    for i in goroskop_text:
        if i != '':
            goroskop_text_1.append(i)
    for i in range(12):
        print('{}resurses/goroskop_files/{}.txt'.format(start_path, bot_variable.spisok_znakov[i]))
        print(goroskop_text_1[i])
        filegor = open('{}resurses/goroskop_files/{}.txt'.format(start_path, bot_variable.spisok_znakov[i]), 'w',
                       encoding='utf-8')
        filegor.write(goroskop_text_1[i][1::])
        filegor.close()


# вычисление знака зодиака пользователя по дате рождения


def goroscop_user(bd_date):
    if bd_date[1] == '1':
        if int(bd_date[0]) < 20:
            return 'capricorn'
        else:
            return 'aquarius'
    elif bd_date[1] == '2':
        if int(bd_date[0]) < 19:
            return 'aquarius'
        else:
            return 'pisces'
    elif bd_date[1] == '3':
        if int(bd_date[0]) < 21:
            return 'pisces'
        else:
            return 'aries'
    elif bd_date[1] == '4':
        if int(bd_date[0]) < 21:
            return 'aries'
        else:
            return 'taurus'
    elif bd_date[1] == '5':
        if int(bd_date[0]) < 21:
            return 'taurus'
        else:
            return 'gemini'
    elif bd_date[1] == '6':
        if int(bd_date[0]) < 22:
            return 'gemini'
        else:
            return 'cancer'
    elif bd_date[1] == '7':
        if int(bd_date[0]) < 23:
            return 'cancer'
        else:
            return 'leo'
    elif bd_date[1] == '8':
        if int(bd_date[0]) < 23:
            return 'leo'
        else:
            return 'virgo'
    elif bd_date[1] == '9':
        if int(bd_date[0]) < 23:
            return 'virgo'
        else:
            return 'libra'
    elif bd_date[1] == '10':
        if int(bd_date[0]) < 23:
            return 'libra'
        else:
            return 'scorpio'
    elif bd_date[1] == '11':
        if int(bd_date[0]) < 22:
            return 'scorpio'
        else:
            return 'sagittarius'
    elif bd_date[1] == '12':
        if int(bd_date[0]) < 22:
            return 'sagittarius'
        else:
            return 'capricorn'


# формирование ответа с погодой
def get_wind_direction(deg):
    l = ['С ', 'СВ', ' В', 'ЮВ', 'Ю ', 'ЮЗ', ' З', 'СЗ']
    for i in range(0, 8):
        step = 45.
        min = i * step - 45 / 2.
        max = i * step + 45 / 2.
        if i == 0 and deg > 360 - 45 / 2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res


def get_city_id(s_city_name):
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                               'APPID': bot_variable.appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    city_id = data['list'][0]['id']

    assert isinstance(city_id, int)
    return city_id


# Запрос текущей погоды
def request_current_weather(city_id):

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': bot_variable.appid})

    data = res.json()
    print(data)
    result_1 = bot_variable.im_text[data['weather'][0]['description']] + ' ' + data['weather'][0]['description'] + \
               "\nТемпература сейчас: " + str(round(data['main']['temp'])) + '°C' + \
               "\nОщущается как: " + str(round(data['main']['feels_like'])) + '°C' + \
               "\nВетер: " + str(round(data['wind']['speed'])) + 'м/с' + get_wind_direction(data['wind']['deg'])

    return result_1


# Прогноз
def request_forecast(city_id):

    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': bot_variable.appid})

    data = res.json()
    result_2 = []
    for i in data['list']:
        if (i['dt_txt'])[11:16] != '15:00' and (i['dt_txt'])[11:16] != '21:00' and (i['dt_txt'])[11:16] != '03:00' and (
                                                                                                                       i[
                                                                                                                           'dt_txt'])[
                                                                                                                       11:16] != '09:00':
            result_2.append(
                bot_variable.im_text_day[(i['dt_txt'])[11:16]] + (i['dt_txt'])[8:10] + '.' + (i['dt_txt'])[5:7] + ' ' + \
                '{0:+3.0f}'.format(i['main']['temp']) + '°C' + \
                '{0:2.0f}'.format(i['wind']['speed']) + " м/с " + \
                get_wind_direction(i['wind']['deg']) + ' ' + \
                bot_variable.im_text[i['weather'][0]['description']])

    return '\n'.join(result_2)


def wheather_today(city: str):
    try:
        city = city.replace(" ", "-")
        request = requests.get("https://sinoptik.ua/погода-" + city)
        b = bs4.BeautifulSoup(request.text, "html.parser")
        city_ids = get_city_id(city)
        article = b.find_all("div", "description")
        result = request_current_weather(city_ids)
        result += '\n' + article[0].getText()
        return result
    except IndexError:
        return 'Что-то пошло не так...'


def wheather_tomm(city: str):
    try:
        city = city.replace(" ", "-")
        request = requests.get("https://sinoptik.ua/погода-" + city)
        b = bs4.BeautifulSoup(request.text, "html.parser")
        city_ids = get_city_id(city)
        return request_forecast(city_ids)
    except IndexError:
        return 'Что-то пошло не так...'


# преобразование текста сообщения
def text_transform(text_message: str):
    evtxt = ''
    for i in range(0, len(text_message)):
        if not text_message[i] in bot_variable.list_pnct_marks or (i == 0 and text_message[i] == '!'):
            evtxt += text_message[i]
    if evtxt == '':
        text_message = text_message.lower()
    else:
        text_message = evtxt.lower()
    if text_message[:33:] == 'club178949259|violet copernicium ':
        text_message = text_message[33::]
        flkv = True
    else:
        flkv = False
    if text_message[:29:] == 'club178949259|@club178949259 ':
        text_message = text_message[29::]
        flkv2 = True
    else:
        flkv2 = False
    return flkv, flkv2, text_message


# получение даты рождения, имени и фамилии, города
def requests_fio_city_bddate(event):

    fio_json = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
        event.obj.from_id) + "&fields=bdate, city&access_token=" + token + "&v=5.92").json()

    first_name = fio_json["response"][0]["first_name"]
    last_name = fio_json["response"][0]["last_name"]

    try:
        city_user = fio_json["response"][0]["city"]["title"]
        flag_city = True
    except KeyError:
        city_user = None
        flag_city = False

    try:
        bd_date = fio_json["response"][0]["bdate"]
        flagbddate = True

    except KeyError:
        flagbddate = False
        bd_date = None
    return city_user, flag_city, first_name, last_name, bd_date, flagbddate


# получение текущего дня
def today_without_zero():
    day = time.strftime("%d", time.localtime())
    if day[0] == '0':
        day = day[1::]
    return day


# получение имени и фамилии по айди
def name_about_id(user_id: str):

    fio_1 = requests.get("https://api.vk.com/method/users.get?user_ids=" + user_id
                         + "&fields=bdate&access_token=" + token + "&v=5.92").json()

    first_name_1 = fio_1["response"][0]["first_name"]
    last_name_1 = fio_1["response"][0]["last_name"]
    return [first_name_1, last_name_1]


# получение списка участников чата по его айди
def dialog_users_list(chat_id: str):
    # chat_id = 1
    f_1 = open('{}token.txt'.format(start_path), 'r')
    token_1 = f_1.read()
    f_1.close()

    list_users = requests.get("https://api.vk.com/method/messages.getConversationMembers?peer_id=" +
                              str(2000000000 + int(chat_id)) + "&access_token=" + token_1 + "&v=5.131").json()

    count_users = (list_users["response"]["count"])
    list_users_rtrn = []
    for i in (list_users["response"]["profiles"]):
        if "type" not in i:
            list_users_rtrn.append(str(i["id"]) + " " + i["first_name"] + " " + i["last_name"])
    return count_users, list_users_rtrn
