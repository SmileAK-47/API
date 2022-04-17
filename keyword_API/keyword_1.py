#接口自动化关键字

import requests

class keyDemo(object):
    #定义get
    def get(self,url,params=None,headers=None):
        return requests.get(url=url,params=params,headers=headers)
    #定义post
    def post(self,url,headers=None,data=None):
        return requests.post(url=url,headers=headers,json=data)

#测试