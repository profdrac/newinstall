import requests
import json
import time
import os

sub = 'photoshoprequest'
timer = 60
download_free = False
thumb = True
show_onlypaid = True

def get_post():
    try:
        base_url = f'https://www.reddit.com/r/'+sub+'/new.json?count=1&t=all'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
        return request.json()
    except:
        return

def download_pic(new_post):
    try:
        img = new_post['data']['children'][0]['data']['url_overridden_by_dest']
        imgname = os.path.basename(img)
        if imgname[-4]=='.' or imgname[-4]=='w':
            img_data = requests.get(img).content
            with open('/home/ashu/shop/'+imgname, 'wb') as handler:
                handler.write(img_data)
        return
    except:
        return

def download_gallery(new_post):
    for i in range(5):
        try:
            img = list(new_post['data']['children'][0]['data']['media_metadata'].values())[i]['s']['u'].replace('amp;','')
            simg = img[0:img.find('?')]
            imgname = os.path.basename(simg)
            if imgname[-4]=='.' or imgname[-4]=='w':
                img_data = requests.get(img).content
                with open('/home/ashu/shop/'+imgname, 'wb') as handler:
                    handler.write(img_data)    
        except:
            break
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

def download(new_post):
    if 'media_metadata' in new_post['data']['children'][0]['data']:
        download_gallery(new_post)
    else:
        download_pic(new_post)
    return

while True:
    new_post = get_post()
    title = new_post['data']['children'][0]['data']['title'].replace("'","")
    fi = '/home/ashu/.scripts/last'
    with open(fi,'r') as f: tit = f.readline()
    if tit != title:
        flair = new_post['data']['children'][0]['data']['link_flair_css_class']
        if flair=='paid' or title.lower().find('pay')!=-1 or title.lower().find('tip')!=-1 or title.find('$')!=-1:
            cmd = 'notify-send -a "psr" -u critical '+"'  '"+" '"+title+"'"
            download(new_post)
        else:
            if show_onlypaid==True:
                time.sleep(timer)
                continue
            cmd = 'notify-send -a "psr" '+"'  '"+" '"+title+"'"
            if download_free==True: download(new_post)
        if thumb==True:
            download_thumb(new_post)
            os.system(cmd+' -i "/home/ashu/.scripts/thumb.jpg"')
        else: os.system(cmd)
        f = open(fi,'w')
        f.write(title)
        f.close()
    time.sleep(timer)
