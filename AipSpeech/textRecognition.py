# encoding:utf-8

import requests
import base64

'''
通用文字识别（高精度版）
'''

def get_access_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
           'd3505rqkfipyzDKqpRBr7oCp&client_secret=3hWQ736DLq2Oxh8pybnww2GknWtZzueB'
    # host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
    #        'eZfr4d4wDu1Ike3Fw4KFobuF&client_secret=TEIvgHjjVRRPEtqbG9B9XtK4UzQY3wLj'
    response = requests.get(host)
    if response:
        return response.json()["access_token"]

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('../images/img2txt.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = get_access_token()
print(access_token)
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())