import requests
import json

f = open('test.txt', 'w', encoding='utf-8')
offset = 0

while offset < 31800:
    response = requests.get(
        'https://api.vk.com/method/wall.get?owner_id=&access_token=&v=5.0', params={
          'owner_id': 60178926,
          'access_token': 'f5a4ce13f5a4ce13f5a4ce138bf5d42d55ff5a4f5a4ce13ab29647f2c26a1909abeca78',
          'offset': offset,
          'count': 100}).json()
    offset += 100
    s = json.dumps(response)
    s = json.loads(s)
    for i in s['response']['items']:
        if i['text'] == '':
            continue
        else:
            f.write(i['text'] + '\n----\n')