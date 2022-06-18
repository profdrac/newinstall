# thememe v1
# Downloads wallpaper from /r/wallpaper and sets system-theme using wal

import requests
import json
import time
import os

picpath = '/home/ashu/Pictures/'

def get_post():
    try:
        base_url = f'https://www.reddit.com/r/wallpaper/hot.json?count=1&t=hour'
        request = requests.get(base_url, headers = {'User-agent': 'thememe'})
        return request.json()
    except:
        return

def download_pic(new_post):
    try:
        img = new_post['data']['children'][0]['data']['url_overridden_by_dest']
        imgname = os.path.basename(img)
        if os.path.isfile(picpath+imgname):
            return imgname
        if imgname[-4]=='.' or imgname[-4]=='w':
            img_data = requests.get(img).content
            with open(picpath+imgname, 'wb') as handler:
                handler.write(img_data)
            return imgname
    except:
        return

def download_gallery(new_post):
    try:
        img = list(new_post['data']['children'][0]['data']['media_metadata'].values())[0]['s']['u'].replace('amp;','')
        simg = img[0:img.find('?')]
        imgname = os.path.basename(simg)
        if os.path.isfile(picpath+imgname):
            return imgname
        if imgname[-4]=='.' or imgname[-4]=='w':
            img_data = requests.get(img).content
            with open(picpath+imgname, 'wb') as handler:
                handler.write(img_data)
            return imgname
    except:
        return

def download(new_post):
    if 'media_metadata' in new_post['data']['children'][0]['data']:
        return download_gallery(new_post)
    else:
        return download_pic(new_post)

new_post = get_post()
print('Getting link...')
cmd = 'notify-send -a "newtheme" '+"'  '"+" 'New theme set successfully!'"
print('Downloading wallpaper...')
pic = download(new_post)
print('Setting theme...')
os.system('wal -i '+picpath+pic)
os.system('(killall dunst&dunst &)')
time.sleep(1)
os.system(cmd)
