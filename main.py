from aiocqhttp.default import on_message, send, api, run,CQHttp
from modle import *

bot = CQHttp()
ex = mess()
state_num = 0 #初始状态
help_text=""" 查题，微博热榜，土味情话，毒鸡汤"""
async def stanum(m,event):
    global state_num
    if state_num == 1:
        data=ser_title(m)
        await send(event,data)

@on_message
async def handle_msg(event):
    global state_num
    message = event.message
    uid = event.user_id
    if message == "back":
        state_num=0
        await send(event,"状态已归零")
    elif state_num != 0:
        await stanum(message,event)
    elif message == "help":
        await send(event,help_text)
    elif message == "查题":
        state_num=1
        await send(event,'已进入答题模式,输入back退出')
    elif message == "舔狗":
        data =ex.get_tiangou()
        await api.send_private_msg(user_id=event.user_id, message=data)
    elif message == "毒鸡汤":
        data =ex.get_soul()
        await api.send_private_msg(user_id=event.user_id, message=data)
    elif message == "微博热榜":
        data =ex.get_weibo
        await api.send_private_msg(user_id=event.user_id, message=data)
    elif message == "土味情话":
        data =ex.get_tuwei()
        await api.send_private_msg(user_id=event.user_id, message=data)






run(host='127.0.0.1', port=8080)