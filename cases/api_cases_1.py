import configparser
import unittest
from API_keyword.keyword_method import method
from ddt import ddt, file_data


# import pyyaml

# 创建一个test框架

@ddt
class apiCase(unittest.TestCase):

   #公共部分 初始化，
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = None
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        cls.dz = method()

        # 测试用例

    @file_data('../API_data/login.yaml')
    def test_1_api_login(self, **kwargs):
        # 实例化

        url = self.url + kwargs['path']
        # print(url)
        # 接口测试
        res = self.dz.post(url=url, headers=kwargs['headers'], data=kwargs['data'])

        token = self.dz.get_text(res.text, 'access_token')
        # token =dz.get_text(res.text,'')
        print(token)
        # self.assertEqual(first=kwargskwargs['text'],second=value,msg='失败')
        # self.assertEqual(first=200,second=code['code'],msg='失败')

    @file_data('../API_data/member.yaml')
    def test_2_api_member(self,**kwargs):
        url = self.url + kwargs['path']
        # print(url)
        # 接口测试
        headers = kwargs['headers']

        headers['Authorization'] = 'Bear'+self.token
        print(headers['Authorization'])
        res = self.dz.get(url=url, headers=headers)

        # token = self.dz.get_text(res.text, 'access_token')
        # token =dz.get_text(res.text,'')
        print(res.text)
    #     print("111")
    #     print(self.token)


    def setUp(self) -> None:
        pass
if __name__ == '__main__':
    unittest.main()
