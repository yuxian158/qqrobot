import re


def ser(ch: str) -> str:
    with open("../../qqrobot/qqrobot/exam/dome.txt", 'r', encoding='utf8') as f:
        read = f.readlines()
        for lin in read:
            if re.match(".*" + ch + ".*", lin):
                return lin


print(ser("马克思主义中国化"))
