import unittest
from Tools.HTMLTestReportCN import HTMLTestRunner
import time, os

if __name__ == '__main__':
    # 加载当前目录
    case_dir = './Case/'
    # 加载当前目录下test开头的.py文件
    discove = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
    # 定义报告目录
    if not os.path.exists('./Reports/'):
        os.makedirs('./Reports/')
    file_dir = './Reports/'
    # 定义报告名称格式
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # 报告完整路径和名称
    file_name = file_dir + now_time + "Report.html"
    with open(file_name, "wb") as f:
        # 实例化HTMLTestRunenr对象，传入报告文件流f
        runner = HTMLTestRunner(stream=f, verbosity=2, title='deals_V4接口自动化测试报告', description="V4接口针对广告_产品的筛选/推荐,前端查询/排序各个参数校验", tester="Jerry")
        runner.run(discove)
