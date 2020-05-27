import requests


class mess():
    url = 'https://v1.alapi.cn/api/'

    def _get_url(self, state):
        url = self.url + state
        payload = "format=json"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return response

    def get_tiangou(self):  # 舔狗日记
        data = self._get_url('dog')
        return data['data']['content']

    def get_tuwei(self):  # 土味情话
        data = self._get_url('qinghua')
        return data['data']['content']

    def get_soul(self):  # 毒鸡汤
        data = self._get_url('soul')
        return data['data']['title']

    @property
    def get_weibo(self):
        res = ''
        data = self._get_url('new/wbtop')['data']
        for i in data:
            res = res + i['hot_word'] + "  热度: " + i['hot_word_num'] + '\n'
        return res
