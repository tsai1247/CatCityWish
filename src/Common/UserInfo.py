from dotenv import load_dotenv
from os import getenv
import glob
import base64
import requests
import json
from datetime import datetime

class UserInfo:
    def __init__(self, catcityPath='C:\Program Files\貓之城') -> None:
        # userInfoPath = f'{catcityPath}\GameClient\CatFantasy\CatFantasy_Data'
        # userInfoList = glob.glob(f'{userInfoPath}\*.txt')

        # if len(userInfoList) == 0:
        #     raise RuntimeError("Path not found")

        # userInfo_encoded = open(userInfoList[0], 'r', encoding='utf-8').read()
        # userInfo = json.loads(base64.b64decode(userInfo_encoded))

        # self.username = userInfo['username']
        # self.sign = userInfo['sign']
        # self.openId = str(userInfo['openId'])
        self.sessionId = None
        self.expireAt = datetime.timestamp(datetime.now())

    def login(self, sessionId = None):
        load_dotenv()
        if sessionId is not None:
            self.sessionId = sessionId
            self.expireAt = datetime.timestamp(datetime.now()) + 1800
            return
        
        if self.sessionId is not None and self.expireAt > datetime.timestamp(datetime.now()):
            return

        self.accessToken = getenv('accessToken')
        self.clientAppId = getenv('clientAppId')
        self.playerId = getenv('playerId')

        URL = 'https://cat-tw.fungoglobal.com/webLogQuery/autoLogin'
        payload = {
            "clientAppId": self.clientAppId,
            "accessToken": self.accessToken
        }

        res = requests.post(URL, json = payload)
        response = json.loads(res.text)
        self.sessionId = response["data"]["sessionId"]
        self.expireAt = response["data"]["expireAt"]

    def callLog(self, page = 1, pageSize = 10):
        print(f'\r正在抓取第{page}頁', end='')
        URL = 'https://cat-tw.fungoglobal.com/webLogQuery/callLog'
        payload = {
            "sessionId": self.sessionId,
            "playerId": self.playerId,
            "lang": "zh-tw",
            "pageSize": pageSize,
            "page": page
        }

        res = requests.post(URL, json = payload)
        response = json.loads(res.text)
        return response['data']['total'], response['data']['list']

