import requests
from aip import AipImageClassify, AipSpeech

""" 你的 APPID AK SK """
APP_ID = '25211913'
API_KEY = 'H01HCGlxH564BWG6UcK8TDVv'
SECRET_KEY = 'S0gAUjjGlIY4LizaBctDOGF8s4iDfOU7'

client_img = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
client_speech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


class Aip:
    def __init__(self, filePath):
        self.img = self.get_file_content(filePath)

    """ 读取图片 """

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    """ 调用通用物品和场景识别 """

    def advance_general_reg(self):
        options = {}
        options["baike_num"] = 5  # 返回百科信息的结果数
        return client_img.advancedGeneral(self.img, options)

    """ 语音合成 """

    def speech_synthesis(self):
        options = {}
        options['vol'] = 5  # 音量5
        options['spd'] = 3  # 语速3
        options['pit'] = 5  # 音调5
        text, file_name = self.get_information()
        ret = client_speech.synthesis(text, 'zh', 1, options)
        if not isinstance(ret, dict):
            with open("./audios/" + file_name + ".mp3", 'wb') as f:
                f.write(ret)

    """ 返回百科信息 """

    def get_information(self):
        ret = self.advance_general_reg()
        # print(ret["result"][1]["keyword"])
        # 图片描述，返回百科描述及关键词（作为文件命名）
        print(ret["result"][1]["baike_info"]["description"])
        return ret["result"][1]["baike_info"]["description"], ret["result"][1]["keyword"]

    """返回access_token"""

    def get_access_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
               'eZfr4d4wDu1Ike3Fw4KFobuF&client_secret=TEIvgHjjVRRPEtqbG9B9XtK4UzQY3wLj'
        response = requests.get(host)
        if response:
            return response.json()["access_token"]

    """测试对话机器人"""

    def test_access(self):
        url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + self.get_access_token()
        # post_data = {"version":3.0,"service_id":"S61779","session_id":"[1127231,1127232,1127233]",
        # "log_id":"7758521","request":{"terminal_id":"88888","query":"你好a"}}
        post_data = "{\"version\":\"3.0\",\"service_id\":\"S61779\",\"skill_id\":\"[1127231,1127232,1127233]\"," \
                    "\"session_id\":\"\",\"log_id\":\"7758521\",\"request\":{\"terminal_id\":\"88888\",\"query\":\"你好\"}}"
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=post_data.encode("utf-8"), headers=headers)
        if response:
            print(response.json()["result"]["responses"][0]["actions"][0]["say"])
            return response.json()["result"]["responses"][0]["actions"][0]["say"]


if __name__ == '__main__':
    filePath = "./images"
    aip = Aip(filePath + "/dog.png")
    aip.get_information()
    # aip.speech_synthesis()
    # aip.test_access()
