from aiocqhttp.default import on_message, send, api, run,CQHttp
from modle import *

bot = CQHttp()
ex = mess()
state_num = 0 #初始状态

def stanum(m,cid):
    pass

@on_message
async def handle_msg(event):
    global state_num
    message = event.message
    uid = event.user_id
    if state_num != 0:
        stanum(message,uid)
    elif message == "back":
        state_num=0
        await send(event,"状态已归零")

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