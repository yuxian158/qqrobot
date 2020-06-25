from exam import ser
from others_modles.modle import *

ex = mess()


def reply(problem):
    if problem == "舔狗":
        return ex.get_tiangou()
    elif problem == "毒鸡汤":
        return ex.get_soul()
    elif problem == "微博热榜":
        return ex.get_weibo
    elif problem == "土味情话":
        return ex.get_tuwei()
    else:
        return chat(problem)
