import requests
import json

# 实现一个get请求
url = 'https://test.saanw.com/prod/auth/login'
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Conntent-Type": "application/json;charset=utf-8",
    "Content-Length": "89",
    "Content-Type": "application/json"

}

data = {
    "phone": "13900000076",
    "identifying": "000000",
    "loginType": "mobile",
    # "organizationId": null
}

data_json = json.dumps(data)
res = requests.post(url=url, headers=headers, data=data_json)

# rint(res.status_code)
print(res.text)
# print(res.json())
