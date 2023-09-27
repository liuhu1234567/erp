import requests
import unittest
# from XTestRunner import HTMLTestRunner
from common.TestRunner import HTMLTestRunner

class YouTest(unittest.TestCase):


    def test_timeout(self):
        """测试timeout """
        # r = requests.get("https://httpbin.org/get", params={"key":"value"})
        # print(r.json())
        # self.assertEqual(1+1,2)
        self.assertLessEqual(4, 3,'Test api timeout')

    def test_fail(self):
        """测试fail """
        # r = requests.post("https://httpbin.org/post", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 3)
        # self.assertLessEqual(4, 3, 'Test api timeout！')

    def test_errer(self):
        """测试errer """
        # r = requests.put("https://httpbin.org/put", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 2)
        raise Exception

    def test_pass(self):
        """测试pass """
        # r = requests.put("https://httpbin.org/put", data={"key":"value"})
        # print(r.json())
        print('set--------------')
        self.assertEqual(1 + 1, 2)

    def test_pass2(self):
        """测试pass2 """
        # r = requests.put("https://httpbin.org/put", data={"key":"value"})
        # print(r.json())
        print('set--------------')
        self.assertEqual(1 + 1, 2)

    @unittest.skip('  ')
    def test_skip(self):
        """测试skip """
        # r = requests.delete("https://httpbin.org/delete", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    # HTMLTestRunner
    # suit = unittest.TestSuite()
    # 添加指定用例
    # suit.addTest(YouTest("test_pass"))
    #
    report = "./result/api_result4.html"
    # fp = open(report, 'wb')
    # runner = HTMLTestRunner(stream=fp,
    #                         title='供应链金融接口自动化测试报告',
    #                         language='zh-CN',
    #                         description=['地址：http://app.scf-uat.dianliantech.com'])
    # r = runner.run(suit)
    # fp.close()

    with(open(report, 'wb')) as fp:
        unittest.main(testRunner=HTMLTestRunner(
            stream=fp,
            language='zh-CN',
            title='供应链金融接口测试报告',
            description=['类型：API', '地址：http://app.scf-uat.dianliantech.com', '执行人：Crew']
        ))