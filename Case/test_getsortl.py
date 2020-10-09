import unittest
from Main.run_test import RunTest


class TestGetSortL(unittest.TestCase):

    def setUp(self):
        self.run = RunTest(4)

    def test_001_Web全球英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(1)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_002_Web全球俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(2)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_003_Web美国英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(3)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_004_Web美国俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(4)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_005_Web俄罗斯英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(5)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_006_Web俄罗斯俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(6)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_007_App全球英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(7)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_008_Apр全球俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(8)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_009_App美国英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(9)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_010_App美国俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(10)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_011_App俄罗斯英语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(11)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_012_App俄罗斯俄语_缓存POST方式(self):
        expect, authentic = self.run.go_on_run(12)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_013_参数名_站点错误(self):
        expect, authentic = self.run.go_on_run(13)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_014_参数名_语言错误(self):
        expect, authentic = self.run.go_on_run(14)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_015_参数名_平台错误(self):
        expect, authentic = self.run.go_on_run(15)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_016_参数名_每页数据量错误(self):
        expect, authentic = self.run.go_on_run(16)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_017_参数名_页码错误(self):
        expect, authentic = self.run.go_on_run(17)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_018_参数名_路由错误(self):
        expect, authentic = self.run.go_on_run(18)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_019_参数名_缓存类型错误(self):
        expect, authentic = self.run.go_on_run(19)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_020_参数值_站点错误(self):
        expect, authentic = self.run.go_on_run(20)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_021_参数值_语言错误(self):
        expect, authentic = self.run.go_on_run(21)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_022_参数值_平台错误(self):
        expect, authentic = self.run.go_on_run(22)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_023_参数值_每页数据量错误(self):
        expect, authentic = self.run.go_on_run(23)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_024_参数值_页码错误(self):
        expect, authentic = self.run.go_on_run(24)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_025_参数值_路由错误(self):
        expect, authentic = self.run.go_on_run(25)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_026_参数值_缓存类型错误(self):
        expect, authentic = self.run.go_on_run(26)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_027_参数值_站点为空(self):
        expect, authentic = self.run.go_on_run(27)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_028_参数值_语言为空(self):
        expect, authentic = self.run.go_on_run(28)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_029_参数值_平台为空(self):
        expect, authentic = self.run.go_on_run(29)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_030_参数值_每页数据量为空(self):
        expect, authentic = self.run.go_on_run(30)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_031_参数值_页码为空(self):
        expect, authentic = self.run.go_on_run(31)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_032_参数值_路由为空(self):
        expect, authentic = self.run.go_on_run(32)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_033_参数值_缓存类型为空(self):
        expect, authentic = self.run.go_on_run(33)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    # def test_001(self):
    #     expect, authentic = self.run.go_on_run(1)
    #     self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')
    #
    # def test_002(self):
    #     expect, authentic = self.run.go_on_run(2)
    #     self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')
