# -*- coding: UTF-8 -*-

#from gtts_token import gtts_token
#import led

import logging
import requests
import urllib
import json
import time
from flask import Flask, redirect, url_for, render_template, request, Response
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("settings.cfg")

# "/"으로 접속시 templates 디렉토리의 index.html을 노출


@app.route("/")
def hello():
    return render_template("index2.html")

# "/daumMedia.json"으로 접속시 daum내 뉴스 정보 호출하여 내용 일부 노출.


@app.route("/daumMedia.json")
def getDaumMedia():
    url = "http://media.daum.net/api/service/news/list/important/media.json"
    r = requests.get(url)
    return json.dumps(r.json()["simpleNews"][0])


@app.route("/youtube.json")
def getyoutubeMedia():
    text = request.args.get('text')
    url = "https://www.googleapis.com/youtube/v3/search?key=" + \
        config["DEFAULT"]["YOUTUBE_APP_KEY"] + \
        "&q=" + text + "&maxResults=6&part=snippet"
    r = requests.get(url)
    return json.dumps(r.json())


@app.route("/weatherInfo")
def getWeatherInfo():
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')

    headers = {'appKey': config["DEFAULT"]["SKPLANET_APP_KEY"]}
    url = 'http://apis.skplanetx.com/weather/current/hourly?version=1&lat=' + \
        (str(latitude)) + '&lon=' + (str(longitude))

    r = requests.get(url, headers=headers)
    return json.dumps(r.json()["weather"]["hourly"][0])

#  GPIO LED ON


@app.route("/ledon.json")
def ledon():
    #    led.ledon()
    return json.dumps({"txt": "불을 켰습니다."})

# GPIO LED OFF


@app.route("/ledoff.json")
def ledoff():
    #    led.ledoff()
    return json.dumps({"txt": "불을 껐습니다."})


# 구글 TTS 를 사용하기 위한 token 생성
# def generateGttsToken(text):
#    token = gtts_token.Token().calculate_token(text)
#    return token

# 구글 TTS 를 통한 음성 출력
#@app.route("/gtts.json")
# def gtts():
#    text = request.args.get('text')
#    #url = 'https://translate.google.com/translate_tts?q=' + text + '&tl=ko&client=t&tk='
#    url = 'https://translate.google.com/translate_tts'
#    token = generateGttsToken(text)
#    paramMap = {"q": text, "tl": "ko", "client": "t", "tk": token}
#
#    param = urllib.parse.urlencode(paramMap)
#    print(url + '?' + param)
#    r = requests.get(url + '?' + param)
#    resultObj = {"url": url + '?' + param}
#    return json.dumps(resultObj)
#    # return render_template("gtts.html", url=url + token)
#
# 구글 TTS 를 통한 음성 출력
@app.route("/gtts.json")
def gtts():
    text = request.args.get('text')
    #url = 'https://translate.google.com/translate_tts?q=' + text + '&tl=ko&client=t&tk='
    url = 'https://translate.google.com/translate_tts'
    token = gtts_token.Token().calculate_token(text)    # 구글 TTS 를 사용하기 위한 token 생성
    paramMap = {"q": text, "tl": "ko", "client": "t", "tk": token}

    param = urllib.parse.urlencode(paramMap)
    print(url + '?' + param)
    r = requests.get(url + '?' + param)
    resultObj = {"url": url + '?' + param}
    return json.dumps(resultObj)
    # return render_template("gtts.html", url=url + token)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
