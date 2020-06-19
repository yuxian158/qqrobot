import requests
import time

SEND = 'https://m.weibo.cn/api/chat/send'
RECV = 'https://m.weibo.cn/api/chat/list?uid=5175429989&count=10&unfollowing=0'


def __read_headers():
    real = {}
    f = open('hend.txt', encoding='utf-8')

    line = f.readline().strip()
    while line:
        key = line.split(":")[0]
        # firefox里的原始头冒号后面会多出一个空格，需除去
        real[key] = line[len(key) + 1:].strip()
        line = f.readline().strip()
    f.close()
    return real


def __send_message(mess: str):
    hend = __read_headers()
    data = dict(uid=5175429989,
                content=mess,
                st=hend['x-xsrf-token'])
    requests.post(SEND, headers=__read_headers(), data=data)


def __get_requesion():
    data = requests.get(RECV, headers=__read_headers()).json()
    back = data['data']['msgs'][0]['text']
    return back


def chat(mess):
    __send_message(mess)
    time.sleep(2)
    mes = __get_requesion()
    return mes
