import unittest
from config.all_path import case_api_dir, project_path, report_dir
from common.BeautifulReport.BeautifulReport import BeautifulReport
from common.do_config import report_name, upload_MeterShpere, upload_robot, upload_email
from common.upload_report import insert_report, get_file_url
from common.do_robot import send_robot
from common.do_email import send_email
from common.TestRunner import HTMLTestRunner



def create_suite():
    """创建测试套件"""
    case = unittest.TestLoader().discover(case_api_dir, pattern='*.py', top_level_dir=project_path)
    suite = unittest.TestSuite()
    suite.addTests(case)
    return suite


def unittest_beautiful():
    """使用BeautifulReport生成报告"""
    suite = create_suite()
    runner = BeautifulReport(suite)
    runner.report(filename=report_name, report_dir=report_dir, description='接口自动化测试报告')

def unittest_xtestrunner():
    report = report_dir + '\\' + report_name
    fp = open(report, 'wb')
    suite = unittest.TestLoader().discover(case_api_dir, pattern='*.py', top_level_dir=project_path)
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试报告',
                            language='zh-CN',
                            description=['地址：http://app.scf-uat.dianliantech.com'])
    r = runner.run(suite)
    fp.close()

def send_report():
    """发送报告"""
    file_url = None
    if upload_MeterShpere or upload_robot or upload_email:
        file_url = get_file_url(report_name)
    if upload_MeterShpere:
        insert_report('cloud', report_name, file_url)
    if upload_robot:
        send_robot(file_url)
    if upload_email:
        send_email(file_url)


if __name__ == '__main__':
    # create_suite()
    unittest_beautiful()
    # unittest_xtestrunner()
    send_report()
