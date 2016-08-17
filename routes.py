# -*- coding: UTF-8 -*-

import logging
import requests
import json
from flask import Flask, redirect, url_for, render_template, request, Response
from gtts_token import gtts_token
import led

app = Flask(__name__)
domain = 'http://127.0.0.1:5000'


# "/"으로 접속시 templates 디렉토리의 index.html을 노출
@app.route("/")
def hello():
    return render_template("index.html")


# "/daumMedia.json"으로 접속시 daum내 뉴스 정보 호출하여 내용 일부 노출.
@app.route("/daumMedia.json")
def getDaumMedia():
    url = "http://media.daum.net/api/service/news/list/important/media.json"
    r = requests.get(url)
    return json.dumps(r.json()["simpleNews"][0])


# 구글 TTS 를 통한 음성 출력
@app.route("/gtts")
def gtts():
    text = request.args.get('text')
    url = 'https://translate.google.com/translate_tts?q=' + text + '&tl=ko&client=t&tk='
    token = gtts_token.Token().calculate_token(text) # 구글 TTS 를 사용하기 위한 token 생성
    r = requests.get(url + token)

    return render_template("gtts.html", url=url + token)


#  GPIO LED ON
@app.route("/ledon")
def ledon():
    led.ledon()
    return

# GPIO LED OFF
@app.route("/ledoff")
def ledoff():
    led.ledoff()
    return

if __name__ == "__main__":
    app.run(debug=True)
