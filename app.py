# -*- coding: utf-8 -*-
import datetime
import json
import re
import sys

import requests
from requests.structures import CaseInsensitiveDict

header = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;zfsoft',
}

with open('app-user.json', encoding='utf-8') as f:
    users = json.load(f)

for user in users:
    try:
        user["redirectUrl"] = "https://myapp.zjgsu.edu.cn/home/index"
        user["clientId"] = "qnFZATsB6D25EnZeII"
        user["mobileBT"] = "11111111-1111-1111-1111-111111111111"

        s = requests.session()
        res = s.post('https://uia.zjgsu.edu.cn/cas/mobile/getAccessToken', data=user, headers=header)
        access_token = res.json()['access_token']
        s.get('https://uia.zjgsu.edu.cn/cas/login?service=https://myapp.zjgsu.edu.cn/home/index&access_token=' + access_token + '&mobileBT=' + user['mobileBT'])

        res = s.get('https://ticket.zjgsu.edu.cn/stucheckservice/auth/login/stuCheck', headers=header)
        referer = res.history[-1].headers['location']
        token = re.search(R'\?token=(.+?)&', referer).group(1)
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer " + token
        headers["token"] = token
        headers["Content-Type"] = "application/json"
        if sys.argv[1] == 'ticket':
            data = """{"place": "浙江省,杭州市,钱塘区,学正街18号","coordinate": "120.388529,30.308752"}""".encode('utf-8')
            res = s.get('https://ticket.zjgsu.edu.cn/stucheckservice/service/getchecklist', headers=headers, data=data)
            if len(res.json()['data']['items']) > 0:
                print(datetime.datetime.now().strftime('%Y-%m-%d'), '报送情况： *主动报送*')
                continue
            res = s.post('https://ticket.zjgsu.edu.cn/stucheckservice/service/stuclockin', headers=headers, data=data)
            print(datetime.datetime.now().strftime('%Y-%m-%d'), '报送情况：' + (
                '成功打卡' if res.json()['code'] == 20000 else '打卡失败！！！！！！'
            ))
        elif sys.argv[1] == 'yzy':
            # 虽然你什么都不传输过去也是可以的，但是感觉还是得给学校一点面子，毕竟让辅导员看到我啥都没填写就推送的也不太好是不是啊，所以就随便写一点把
            data = """{"currentResd":":)","fromHbToZj":"C","fromWtToHz":"B","meetCase":"C","travelCase":"D",
            "medObsv":"B","belowCase":"D","hzQrCode":"A","specialDesc":"无","deviceId":":)","fromDevice":"",
            "isNewEpid":"否","location":"","coordinate":":-("}""".encode('utf-8')
            res = s.post('https://yzy.zjgsu.edu.cn/cloudbattleservice/service/add', headers=headers, data=data)
            print(datetime.datetime.now().strftime('%Y-%m-%d'), '报送情况：' + (
                '成功打卡' if res.json()['code'] == 20000 else '打卡失败！！！！！！'
            ))
        else:
            print(datetime.datetime.now().strftime('%Y-%m-%d'), '参数错误')
    except Exception as e:
        print(datetime.datetime.now().strftime('%Y-%m-%d'), '报送情况：打卡失败！！！！！！')
        continue
