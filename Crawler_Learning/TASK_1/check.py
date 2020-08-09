#!/usr/bin/python
#-*-coding: utf8-*-

#TASK测试用例检查
import unittest
#导入被检查的用例的模块
import  Crawler_Learning.TASK_1.SpiritBoy.TestTask as jhptest

def test_cases():
    test_suite = unittest.TestSuite()
    #添加测试用例
    #SpiritBoy
    test_suite.addTest(jhptest.TestTask("test_1"))
    print("SpiritBoy's test cases is finished")

    return test_suite


if __name__ == "__main__":
    unittest.main(defaultTest="test_cases")
