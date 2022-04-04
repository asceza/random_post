from flask import Flask, request, session, make_response, redirect
import requests
import random
from datetime import datetime
import re

app = Flask(__name__)

vc_max_post = 393000
dft_max_post = 1146666
tj_max_post = 475000


@app.route('/vc')
def get_vc_data():
    return get_data()


def get_data():
    random_int = random.randint(0, vc_max_post)
    api_url = f'https://api.vc.ru/v2.1/content?id={random_int}'
    # api_url = f'https://api.vc.ru/v2.1/content?id=136510'
    direct_url = f'https://vc.ru/{random_int}'
    print(direct_url)
    json_data = requests.get(api_url).json()
    try:
        subsite_avatar_url = json_data['result']['subsite']['avatar']['data']['uuid']
        subsite_avatar_url = f'https://leonardo.osnova.io/{subsite_avatar_url}/-/scale_crop/32x32/'
        # print(subsite_avatar_url)
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

        res = make_response(f'''
        <div class="header_content">
          <img src="{subsite_avatar_url}" width="20" alt="">
          <span class='subsite fw-bold'>{subsite_name}</span>
          <span class='author'>{author}</span>
          <span class='date'>{date}</span>
        </div>
        <div class='title fw-bold fs-5 '>{title}</div>
        <div class="post_body">
          <span class='fw-light lh-base fs-6'><a href="{direct_url}" target="_blank">{post_body}</a></span>
        </div>
        <div class="footer_content">
          <img src="./data/comment.png" width="20" alt="*">
          <span class='comment'>{comments}</span>
          <img src="./data/love.png" width="18" alt="*">
          <span class='like'>{likes}</span>
          <img src="./data/view.png" width="20" alt="*">
          <span class='view'>{views}</span>
        </div>''')
        # res = make_response('what')
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res
    except:
        res = make_response(
            f'Страница <a href="{direct_url}" target="_blank">{direct_url}</a> не существует')
        res.headers['Access-Control-Allow-Origin'] = '*'
        return res

    # post_body = json_data['result']['blocks'][0]['data']['raw']
    # print(f'subsite_avatar_url - {subsite_avatar_url}')
    # print(f'subsite_name - {subsite_name}')
    # print(f'author - {author}')
    # print(f'date - {date}')
    # print(f'title - {title}')
    # print(f'likes - {likes}')
    # print(f'comments - {comments}')
    # print(f'views - {views}')
    # print(f'post_body - {post_body}')


if __name__ == "__main__":
    app.run(debug=True)
