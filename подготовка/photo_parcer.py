import requests
import json


def photo_saver(arr, f):
    if 'attachments' not in arr:
        return nbr
    for j in arr['attachments']:
        if j['type'] == 'photo' and j['photo']['photo_604']:
            f.write(j['photo']['photo_604'] + '\n')
            #jpg = requests.get(j['photo']['photo_604'])
            #with open(f'./photo/{nbr}.jpg', 'wb') as file:
            #   file.write(jpg.content)
            #    nbr += 1


offset = 0
f = open('../photo_link.txt', 'w')
while offset < 31800:
    response = requests.get(
        'https://api.vk.com/method/wall.get?', params={
          'owner_id': 60178926,
          'access_token': 'f5a4ce13f5a4ce13f5a4ce138bf5d42d55ff5a4f5a4ce13ab29647f2c26a1909abeca78',
          'offset': offset,
          'count': 100,
          'v': '5.0'}).json()
    print(offset)
    offset += 100
    s = json.dumps(response)
    s = json.loads(s)
    for i in s['response']['items']:
        if i['post_type'] == 'copy':
            nbr = photo_saver(i['copy_history'][0],  f)
        else:
            nbr = photo_saver(i,  f)
