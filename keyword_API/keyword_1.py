#接口自动化关键字

import requests

class keyDemo:
    #定义get
    def get(self,url,params=None,headers=None):
        return requests.get(url=url,params=params,headers=headers)
    #定义post
    def post(self,url,params=None,headers=None):
        return requests.post(url=url,params=params,headers=headers)