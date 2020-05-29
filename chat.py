import requests

data = {
    'key': '3ce2951c30dd74e25803f05efb48dafa',
    'question': 'robot'
}
r = requests.get('http://api.tianapi.com/txapi/robot/index',params=data)
print(r.text)