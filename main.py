from aiocqhttp.default import on_message, send, api, run, CQHttp
from aiocqhttp.message import MessageSegment
from aiocqhttp import Message
from others_modles import reply
bot = CQHttp()


@on_message('private')
async def handle_msg(event):
    message = event.message
    await send(event,reply(message))


@on_message('group')
async def _(event):
    msg = Message(event.message)
    numpad = False
    for seg in msg:
        if seg == MessageSegment.at(event.self_id):
            numpad = True
        if numpad:
            seg = Message(seg).extract_plain_text().strip()
            data = reply(seg)
            await send(event,data)
            numpad = False


run(host='127.0.0.1', port=9090)