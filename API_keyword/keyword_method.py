# 接口自动化关键字

import requests
import jsonpath
import json


class method(object):
    # 定义get
    def get(self, url, params=None, headers=None):
        return requests.get(url=url, params=params, headers=headers)

    # 定义post
    def post(self, url, headers=None, data=None):
        return requests.post(url=url, headers=headers, json=data)

    # 校验字段获取方法
    def get_text(self, res, key):
        if res is not None:
            try:
                # 将res文本转换为json 通过jsonpath解析获取指定值
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '..{0}', format(key))
                # json获取值为list类型，如果获取失败为False
                if value:
                    # 将list 转为string格式
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None
