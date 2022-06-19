import requests
import json
import time
import os

sub = 'photoshoprequest'
timer = 60
thumb = True

def get_post():
    try:
        base_url = f'https://www.reddit.com/r/'+sub+'/new.json?count=1&t=all'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
        return request.json()
    except:
        return

def download_thumb(new_post):
    try:
        turl = new_post['data']['children'][0]['data']['thumbnail']
        tdata = requests.get(turl).content
        with open('/home/ashu/.scripts/thumb.jpg', 'wb') as handler:
            handler.write(tdata)
        return
    except:
        return

while True:
    new_post = get_post()
    title = new_post['data']['children'][0]['data']['title'].replace("'","")
    fi = '/home/ashu/.scripts/last'
    with open(fi,'r') as f:
        tit = f.readline()
    if tit != title:
        download_thumb(new_post)
        flair = new_post['data']['children'][0]['data']['link_flair_css_class']
        if flair=='paid' or title.lower().find('pay')!=-1 or title.lower().find('tip')!=-1 or title.find('$')!=-1: cmd = 'notify-send -a "psr" -u critical '+"'  '"+" '"+title+"'"
        else: cmd = 'notify-send -a "psr" '+"'  '"+" '"+title+"'"
        if thumb==True: os.system(cmd+' -i "/home/ashu/.scripts/thumb.jpg"')
        else: os.system(cmd)
        f = open(fi,'w')
        f.write(title)
        f.close()
    time.sleep(timer)
