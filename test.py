'''
import requests
message_id=15938
rt = requests.get('https://api.vk.com/method/messages.delete?message_ids='+str(message_id)+'&delete_for_all=1&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92')
print(rt.text)
#--------------------------------------------------------------------------------------------------------------
f1 = open("resurses/crocodile_files/new1.txt",mode="w",encoding="utf-8")
f = open("resurses/crocodile_files/new.txt","r")
for line in f:
    line=line.split(" ")
    print(line[5][1:-1:])
    f1.write(line[5][1:-1:]+"\n")
f1.close()
f.close()
#-------------------------------------------------------------------------------------------------------------
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api, time, random
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

session = requests.Session()
vk_session = vk_api.VkApi(token='')
longpoll = VkBotLongPoll(vk_session, '178949259')
vk = vk_session.get_api()
upload = VkUpload(vk_session)

def sent_message_ls(text, user_id):
    message_ids = vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=text
    )
    return message_ids

sent_message_ls("&#8203;",195310233)
#-------------------------------------------------------------------------------------------------------------
import requests, json
message_id=15938
rt = requests.get('https://api.vk.com/method/messages.getConversationMembers?peer_id=2000000001&fields=count,items,profiles1&access_token=b78c719302827104f6346bd3b63df9edd8dee2ef58f84a4e1a4f108cb149fed5d2d53c795ae00ee69f419&v=5.92')
zapros = json.loads(rt.text)

for i in (zapros["response"]['profiles']):
    print(i['id'])
#-------------------------------------------------------------------------------------------------------------
slov=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
slov1={"q":"","w":"","e":"е","r":"","t":"т","y":"у","u":"","i":"","o":"о","p":"р","a":"а","s":"","d":"","f":"","g":"","h":"н",
       "j":"","k":"к","l":"","z":"","x":"х","c":"с","v":"","b":"в","n":"","m":"м","-":" ","3":"з"}
f1 = open("resurses/crocodile_files/new.txt",mode="w",encoding="utf-8")
f = open("resurses/crocodile_files/baza.txt","r")
k=f.read()
k=k.split(") ")
d=[]
for i in k:
    i=i.split(" ")
    i=i[0].lower()
    t=''
    for j in i:
        if j in slov1:
            t += slov1[j]
        else:
            t += j
    d.append(t)
for i in d:
    for j in i:
        if j in slov:
            print(i)
print(d)
for i in d:
    f1.write(i+'\n')
    #print(t)


f1.close()
f.close()
#-------------------------------------------------------------------------------------------------------------
f = open("resurses/crocodile_files/word_rus.txt",mode="r", encoding="utf-8")
f1 = open("resurses/crocodile_files/word_rus1.txt",mode="w", encoding="utf-8")
print(f.encoding)
print(f1.encoding)
k = 0
for line in f:
    k += 1
    a = ''
    for i in line:
        if i == '-':
            a += ' '

        else:
            a += i
    #print(line, a)
    f1.write(a.lower())
    #print(line.split("***"))
print(k)
f.close()
f1.close()
#-------------------------------------------------------------------------------------------------------------
f=open("resurses/crocodile_files/crocodile_hard1.txt", mode="r",encoding="utf-8")
k=0
for line in f:
    k+=1
print(k)
print(f.encoding)
f.close()
#-------------------------------------------------------------------------------------------------------------
import wikipedia
wikipedia.set_lang("ru")
#-----------
g = wikipedia.search("ансамбль")
print(g)
g = wikipedia.page(g[0])
print(g)
#-----------
try:
    g = wikipedia.page("Миропорядок")
    print(g.content.split('\n')[0])
except wikipedia.exceptions.DisambiguationError as e:
    k = e.options
    print(k)
    g = wikipedia.page(k[1])
    print(g.content.split('\n')[0])
#-------------------------------------------------------------------------------------------------------------
import requests
slovo = "фрахтовка"
f = requests.get('https://ru.wiktionary.org/wiki/'+slovo)
print(f.text)
#-------------------------------------------------------------------------------------------------------------
import wikipedia
wikipedia.set_lang("ru")
print(wikipedia.summary("наука"))
#-------------------------------------------------------------------------------------------------------------
import requests
slovo = "время"
key = "dict.1.1.20200214T095827Z.292b7555a3b6a6c5.47588341e06fd43416f84a5289a1f9705c585875"
f= requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='+ key +'&lang=ru-ru&text='+slovo)
print(f.text)
#-------------------------------------------------------------------------------------------------------------
'''
import  requests,bs4
slovo = "улица"
f = requests.get('https://ru.wiktionary.org/wiki/' + slovo)
f.encoding = 'utf-8'
#print(f.text)
k=(bs4.BeautifulSoup(f.text,"html.parser"))
#print(k.find(id="Значение"))
k=k.prettify()
r=f.text.index('class="mw-headline" id="Значение"')
g=f.text[r::].index('\n')
print(f.text[r::].split('\n')[1])
