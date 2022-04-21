# def test(a, *args, **kwargs):
#     print(a)
#     # print b
#     # print c
#     print(args)
#
#     print(kwargs)
#
#
#
# test(1, 2, 3, d='4', e=5)
import unittest


class api(unittest.TestCase):
    def test_1_a(self):
        print("111")
    def test_2_b(self):
        print("222")
    def test_3_c(self):
        print("333")


if __name__ == '__main__':
    unittest.main()