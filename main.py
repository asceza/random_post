# https://cmtt-ru.github.io/osnova-api/v2.1/swagger.html#/Content/getContent

from flask import Flask, request, session, make_response, redirect
import requests
import random
from datetime import datetime
import re

app = Flask(__name__)

vc_max_post = 393000
dft_max_post = 1146666
tjournal_max_post = 475000


@app.route('/<string:domen>')
def get_data(domen):
    data, status = get_data_from_api(domen)
    print(status)
    return data


def get_data_from_api(domen):
    for i in range(5):
        try:
            random_int = random.randint(0, vc_max_post)
            api_url = f'https://api.{domen}.ru/v2.1/content?id={random_int}'
            # api_url = f'https://api.vc.ru/v2.1/content?id=136510'
            direct_url = f'https://{domen}.ru/{random_int}'
            print(direct_url)
            json_data = requests.get(api_url).json()
            subsite_avatar_url = json_data['result']['subsite']['avatar']['data']['uuid']
            subsite_avatar_url = f'https://leonardo.osnova.io/{subsite_avatar_url}/-/scale_crop/32x32/'
            subsite_name = json_data['result']['subsite']['name']
            author = json_data['result']['author']['name']
            date = json_data['result']['date']
            date = datetime.fromtimestamp(date)
            date = date.strftime('%d.%m.%Y')

            try:
                title = json_data['result']['title']
            except:
                title = ''

            likes = json_data['result']['likes']['summ']
            comments = json_data['result']['counters']['comments']
            views = json_data['result']['hitsCount']

            post_body = ''
            for i in range(0, 10):
                try:
                    post_body = post_body + \
                        json_data['result']['blocks'][i]['data']['text'] + "</br>"
                except:
                    post_body = post_body + ''

            post_body = post_body.replace(
                '[', '').replace(']', '').replace('**', '')
            post_body = post_body[0:1000]

            pre_res = make_response(f'''
            <div class="header_content">
              <img src="{subsite_avatar_url}" width="20" alt="">
              <span class='subsite fw-bold'>{subsite_name}</span>
              <span class='author'>{author}</span>
              <span class='date'>{date}</span>
            </div>
            <a href="{direct_url}" target="_blank">
            <div class='title fw-bold fs-5 '>{title}</div>
            <div class="post_body">
              <span class='fw-light lh-base fs-6'>{post_body}</span>
            </div>
            </a>
            <div class="footer_content">
              <img src="./data/comment.png" width="20" alt="*">
              <span class='comment'>{comments}</span>
              <img src="./data/love.png" width="18" alt="*">
              <span class='like'>{likes}</span>
              <img src="./data/view.png" width="20" alt="*">
              <span class='view'>{views}</span>
            </div>''')

            pre_res.headers['Access-Control-Allow-Origin'] = '*'
            res, status = pre_res, True
            break
        except:
            pre_res = make_response(
                f'Страница <a href="{direct_url}" target="_blank">{direct_url}</a> не найдена')
            pre_res.headers['Access-Control-Allow-Origin'] = '*'
            res, status = pre_res, False
            continue

    return res, status

if __name__ == "__main__":
    app.run(debug=True)
