import re
import urllib.parse
import requests

def _ser(ch: str) -> str:
    with open("D:\qqrobot\qqrobot\exam\dome.txt", 'r', encoding='utf8') as f:
        read = f.readlines()
        for lin in read:
            if re.match(".*" + ch + ".*", lin):
                return lin

def ser(ch:str) -> str:
    return _ser(ch)

def ser_title(text):
    title = text
    last = urllib.parse.quote(title)
    data = 'question=' + last
    url = "http://cx.icodef.com/wyn-nb"
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Authorization': ''
    }
    data3 = requests.post(url, headers=headers, data=data)
    return data3.json()['data']