from API_keyword.keyword_method import method
import configparser
import yaml
import json

# 实例化需要的内容
conf = configparser.ConfigParser()
dz = method()

# 获取测试数据 创建data
file = open('../API_data/login_test.yaml', 'r')
data = yaml.load(file, yaml.FullLoader)
# print(data)
# 测试数据
conf.read('../config/config.ini')
# print(conf.get('DEFAULT','url'))

# url =conf.get('DEFAULT','url')+ '/prod/auth/login'
url = conf.get('DEFAULT', 'url') + data["path"]
# print(url)


# 执行测试
# data_json = json.dumps(data["data"])
# print(data_json)
res = dz.post(url=url, headers=data["headers"], data=data["data"])
aa = res.json()
print(aa["code"])

# assert '200' == aa['code']
