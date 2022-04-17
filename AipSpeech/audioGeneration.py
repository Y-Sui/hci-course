from aip import AipSpeech

APP_ID = '25040199'
API_KEY = '4QSHUs3o7KPGV6UWqw3fKYQf'
SECRET_KEY = 'C4BMG8ngBNcKzzBSkwVRluZZQ2kkQIND'

def aipSpeech(str, id):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(str, 'zh', 1, {'spd':6, 'vol': 5, 'per': 106
})
    filename = 'result/audio'
    if not isinstance(result, dict):
        with open(filename + '{}'.format(id) + '.mp3', 'wb') as f:
            f.write(result)
text = []

if __name__ == '__main__':
    file = open('text.txt', encoding='utf-8')
    while True:
        lines = file.readlines(5000)
        if not lines:
            break
        for line in lines:
            text.append(line)
    for i in range(len(text)):
        aipSpeech(text[i], i+1)
