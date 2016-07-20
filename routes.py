# -*- coding: UTF-8 -*-

import requests
import json
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
