#!/usr/bin/python
#-*-coding: utf8-*-
#自己调试用的测试用例，测试完成后，将被检查的用例在
import unittest
#导入被测函数
import  Crawler_Learning.TASK_1.SpiritBoy.J_quick_sort as jhp

#预先写好输入和输出
given_in     = {1:[6,1,34,5,7,9,4,3,5,6],\
         }
expected_out = {1:[1,3,4,5,5,6,6,7,9,34],\
         }
class TestTask(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(jhp.quick_sort(given_in[1]), expected_out[1], msg="SpiritBoy")

if __name__ == "__main__":
    unittest.main()

