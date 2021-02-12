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
    for symbol in range(0, 12):
        file_req = requests.get("http://astroscope.ru/horoskop/ejednevniy_goroskop/" + bot_variable.
                                spisok_znakov[symbol] + ".html")
        file_req.encoding = 'utf-8'
        text_gor = (bs4.BeautifulSoup(file_req.text, "html.parser").find('div', 'col-12'))
        filegor = open('{}resurses/goroskop_files/{}.txt'.format(start_path, bot_variable.spisok_znakov[symbol]), 'w')
        filegor.write(str(str(text_gor).split('\n')[2]).lstrip())
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

# формированиие отдельных частей погоды


def wheather_day(temperature, index_temp, zavtra, image, index_img, wind, index_wind):
    weather = temperature[index_temp + zavtra].getText()
    image1 = image[index_img].getText()
    image1_1 = ''
    for i in image1:
        if i != '\n':
            image1_1 += i
    image1 = image1_1
    image1 = image1.split(', ')
    cloud = bot_variable.im_text[image1[0]]

    if len(image1) == 2:
        if image1[1].find("снег") != -1:
            rain = bot_variable.im_text_2["снег"]
        if image1[1].find("дождь") != -1:
            rain = bot_variable.im_text_2["дождь"]
    else:
        rain = ''

    wind_rtrn = '{}, {} м/с.'.format((str(wind[index_wind + zavtra]).split(' ')[3][7:-5:1]),
                                     (wind[index_wind + zavtra].getText()))
    wind_rtrn = wind_rtrn.split(' ')[1::]
    wind_rtrn[0] = wind_rtrn[0].split('\n')
    wind_rtrn[0] = ''.join(wind_rtrn[0][-1::])
    wind_rtrn = ' '.join(wind_rtrn[:-1:]).replace("\n", "")

    return cloud, weather, wind_rtrn, rain

# формирование ответа с погодой


def wheather(city: str, zavtra: int, zavtra_1: int):
    city = city.replace(" ", "-")
    request = requests.get("https://sinoptik.com.ru/погода-" + city)
    b = bs4.BeautifulSoup(request.text, "html.parser")
    try:
        article = b.find_all("div", "weather__article_description-text")
        temperature = b.find_all("div", "table__temp")
        image = b.find_all("div", "table__time_img")
        wind = b.find_all("div", "table__wind")

        cloud1, weather1, wind1, rain1 = wheather_day(temperature, 0, zavtra, image, 0, wind, 0)
        cloud2, weather2, wind2, rain2 = wheather_day(temperature, 2, zavtra, image, 2, wind, 2)
        cloud3, weather3, wind3, rain3 = wheather_day(temperature, 4, zavtra, image, 4, wind, 4)
        cloud4, weather4, wind4, rain4 = wheather_day(temperature, 6, zavtra, image, 6, wind, 6)

        result = ''
        result = result + ('Ночью : {}{} {},\nВетер: {}.'.format(cloud1, rain1, weather1, wind1)) + '\n\n'
        result = result + ('Утром : {}{} {},\nВетер: {}.'.format(cloud2, rain2, weather2, wind2)) + '\n\n'
        result = result + ('Днём : {}{} {},\nВетер: {}.'.format(cloud3, rain3, weather3, wind3)) + '\n\n'
        result = result + ('Вечером : {}{} {},\nВетер: {}.'.format(cloud4, rain4, weather4, wind4)) + '\n\n'
        result += article[0 + zavtra_1].getText()
        return result
    except IndexError:
        return 'Такого города не найдено.'

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
    if text_message[:24:] == 'club178949259|ботхеработ':
        text_message = text_message[25::]
        flkv = True
    else:
        flkv = False
    if text_message[:28:] == 'club178949259|@club178949259':
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
