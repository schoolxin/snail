# -*- coding:utf-8 -*-
# @FileName  :check_code.py
# @Time      :2023/10/7 9:11
# @Author    :dzz
# @Function  :
import requests, base64
import json


def get_token():
    API_KEY = "zE4aVilOXgn2ZaHIS6659xT0"
    SECRET_KEY = "N83vRZjrdVhmGYRslyajxWEB1yR1N5XN"
    url = "https://aip.baidubce.com/oauth/2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": SECRET_KEY
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=data)

    # token = response.json().get('access_token')
    token = json.loads(response.text).get('access_token')
    # print(token)
    return token


def get_pic(path):
    with open(path, 'rb') as file:
        return file.read()


def get_checkcode():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        'image': base64.b64encode(get_pic(r"F:\study\python\snail\python_scrapy\images\F2S9.jpg")),
        'probability': 'true'
    }

    params = {
        'access_token':get_token()
    }
    resp = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',params=params,headers=headers,data=data)
    print(resp.text)
    print(resp.json().get('words_result')[0].get('words'))


if __name__ == "__main__":
    run_code = 0
    # print(get_token())
    get_checkcode()
