import configparser
import unittest
from API_keyword.keyword_method import method
from ddt import ddt, file_data
# import pyyaml

# 创建一个test框架

@ddt
class ApiCase(unittest.TestCase):

    # 测试用例
    @file_data('../API_data/login.yaml')
    def test_1_api_demo(self, **kwargs):
        # 实例化
        # 实例化需要的内容
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        dz = method()
        # D:\my_code\API\config\config.ini
        url = conf.get('DEFAULT', 'url') + kwargs['path']
        # print(url)
        # 接口测试
        res = dz.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        # aa = res.json()
        print(res.text)
        value = dz.get_text(res.text,'code')
        print(value)
        self.assertEqual(first='200',second=value,msg='失败')

if __name__ == '__main__':
    unittest.main()
