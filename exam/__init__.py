import re


def ser(ch: str) -> str:
    with open("exam\dome.txt", 'r', encoding='utf8') as f:
        read = f.readlines()
        for lin in read:
            if re.match(".*" + ch + ".*", lin):
                return lin
