from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '23642440'
API_KEY = 'hbY0dSexZzqhgrwzehkbjnLT'
SECRET_KEY = 'oSX8LeRe4ZWIXryMEXc9Nzf8Yk7lUriA'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('../images/dog.png')

""" 调用通用物体和场景识别 """
client.advancedGeneral(image)

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体和场景识别 """
client.advancedGeneral(image, options)