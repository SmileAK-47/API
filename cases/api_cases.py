import configparser
import unittest
from API_keyword.keyword_method import method
from ddt import ddt,feed_data

# 创建一个test框架

@ddt
class ApiCase(unittest.TestCase):

    # 测试用例
    @feed_data('../API_data/login.yaml')
    def test_1_api_demo(self,**kwargs):
        # 实例化
        # 实例化需要的内容
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        dz = method()
        url = conf.get('DEFAULT', 'url') + kwargs["path"]
        res = dz.post(url=url, headers=kwargs["headers"], data=kwargs["data"])
        # aa = res.json()
        print(res.json())


if __name__ == '__main__':
    unittest.main()