import unittest
from Main.run_test import RunTest


class TestGetFrontQSortL(unittest.TestCase):

    def setUp(self):
        self.run = RunTest(5)

    def test_001_Web全球英语_前端筛选条件周转化率(self):
        expect, authentic = self.run.go_on_run(1)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_002_Web全球英语_前端筛选条件周点击率(self):
        expect, authentic = self.run.go_on_run(2)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_003_Web全球英语_前端筛选条件周ECPC(self):
        expect, authentic = self.run.go_on_run(3)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_004_Web全球英语_前端筛选条件周曝光(self):
        expect, authentic = self.run.go_on_run(4)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_005_Web全球英语_前端筛选条件周点击(self):
        expect, authentic = self.run.go_on_run(5)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_006_Web全球英语_前端筛选条件周转化(self):
        expect, authentic = self.run.go_on_run(6)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_007_Web全球英语_前端筛选条件周佣金(self):
        expect, authentic = self.run.go_on_run(7)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_008_Web全球英语_前端筛选条件总转化率(self):
        expect, authentic = self.run.go_on_run(8)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_009_Web全球英语_前端筛选条件总点击率(self):
        expect, authentic = self.run.go_on_run(9)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_010_Web全球英语_前端筛选条件总ECPC(self):
        expect, authentic = self.run.go_on_run(10)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_011_Web全球英语_前端筛选条件总曝光(self):
        expect, authentic = self.run.go_on_run(11)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_012_Web全球英语_前端筛选条件总点击(self):
        expect, authentic = self.run.go_on_run(12)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_013_Web全球英语_前端筛选条件总转化(self):
        expect, authentic = self.run.go_on_run(13)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_014_Web全球英语_前端筛选条件总佣金(self):
        expect, authentic = self.run.go_on_run(14)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_015_Web全球英语_前端筛选条件包含文本(self):
        expect, authentic = self.run.go_on_run(15)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_016_Web全球英语_前端筛选条件排除文本(self):
        expect, authentic = self.run.go_on_run(16)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_017_Web全球英语_前端筛选条件排除推荐(self):
        expect, authentic = self.run.go_on_run(17)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_018_Web全球英语_前端筛选条件包含广告商id(self):
        expect, authentic = self.run.go_on_run(18)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_019_Web全球英语_前端筛选条件包含平台(self):
        expect, authentic = self.run.go_on_run(19)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_020_Web全球英语_前端筛选条件产品价格(self):
        expect, authentic = self.run.go_on_run(20)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_021_Web全球英语_前端筛选条件产品类别(self):
        expect, authentic = self.run.go_on_run(21)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_022_Web全球英语_前端筛选条件产品折扣(self):
        expect, authentic = self.run.go_on_run(22)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_023_Web全球英语_前端筛选条件广告类型(self):
        expect, authentic = self.run.go_on_run(23)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_024_Web全球英语_前端筛选条件广告商类别(self):
        expect, authentic = self.run.go_on_run(24)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_025_Web全球英语_前端筛选条件类似广告商(self):
        expect, authentic = self.run.go_on_run(25)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_026_Web全球英语_前端排序条件最后一次点击时间升序(self):
        expect, authentic = self.run.go_on_run(26)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_027_Web全球英语_前端排序条件最后一次点击时间降序(self):
        expect, authentic = self.run.go_on_run(27)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_028_Web全球英语_前端排序条件1天平均点击时间升序(self):
        expect, authentic = self.run.go_on_run(28)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_029_Web全球英语_前端排序条件1天平均点击时间降序(self):
        expect, authentic = self.run.go_on_run(29)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_030_Web全球英语_前端排序条件7天平均点击时间升序(self):
        expect, authentic = self.run.go_on_run(30)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_031_Web全球英语_前端排序条件7天平均点击时间降序(self):
        expect, authentic = self.run.go_on_run(31)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_032_Web全球英语_前端排序条件ES搜索匹配度升序(self):
        expect, authentic = self.run.go_on_run(32)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_033_Web全球英语_前端排序条件ES搜索匹配度降序(self):
        expect, authentic = self.run.go_on_run(33)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_034_Web全球英语_前端排序条件周转化率升序(self):
        expect, authentic = self.run.go_on_run(34)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_035_Web全球英语_前端排序条件周转化率降序(self):
        expect, authentic = self.run.go_on_run(35)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_036_Web全球英语_前端排序条件周点击率升序(self):
        expect, authentic = self.run.go_on_run(36)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_037_Web全球英语_前端排序条件周点击率降序(self):
        expect, authentic = self.run.go_on_run(37)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_038_Web全球英语_前端排序条件周ECPC升序(self):
        expect, authentic = self.run.go_on_run(38)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_039_Web全球英语_前端排序条件周ECPC降序(self):
        expect, authentic = self.run.go_on_run(39)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_040_Web全球英语_前端排序条件周曝光数升序(self):
        expect, authentic = self.run.go_on_run(40)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_041_Web全球英语_前端排序条件周曝光数降序(self):
        expect, authentic = self.run.go_on_run(41)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_042_Web全球英语_前端排序条件周点击数升序(self):
        expect, authentic = self.run.go_on_run(42)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_043_Web全球英语_前端排序条件周点击数降序(self):
        expect, authentic = self.run.go_on_run(43)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_044_Web全球英语_前端排序条件周转化数升序(self):
        expect, authentic = self.run.go_on_run(44)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_045_Web全球英语_前端排序条件周转化数降序(self):
        expect, authentic = self.run.go_on_run(45)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_046_Web全球英语_前端排序条件周佣金升序(self):
        expect, authentic = self.run.go_on_run(46)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_047_Web全球英语_前端排序条件周佣金降序(self):
        expect, authentic = self.run.go_on_run(47)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_048_Web全球英语_前端排序条件总转化率升序(self):
        expect, authentic = self.run.go_on_run(48)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_049_Web全球英语_前端排序条件总转化率降序(self):
        expect, authentic = self.run.go_on_run(49)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_050_Web全球英语_前端排序条件总点击率升序(self):
        expect, authentic = self.run.go_on_run(50)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_051_Web全球英语_前端排序条件总点击率降序(self):
        expect, authentic = self.run.go_on_run(51)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_052_Web全球英语_前端排序条件总ECPC升序(self):
        expect, authentic = self.run.go_on_run(52)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_053_Web全球英语_前端排序条件总ECPC降序(self):
        expect, authentic = self.run.go_on_run(53)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_054_Web全球英语_前端排序条件总曝光数升序(self):
        expect, authentic = self.run.go_on_run(54)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_055_Web全球英语_前端排序条件总曝光数降序(self):
        expect, authentic = self.run.go_on_run(55)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_056_Web全球英语_前端排序条件总点击数升序(self):
        expect, authentic = self.run.go_on_run(56)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_057_Web全球英语_前端排序条件总点击数降序(self):
        expect, authentic = self.run.go_on_run(57)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_058_Web全球英语_前端排序条件总转化数升序(self):
        expect, authentic = self.run.go_on_run(58)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_059_Web全球英语_前端排序条件总转化数降序(self):
        expect, authentic = self.run.go_on_run(59)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_060_Web全球英语_前端排序条件总佣金升序(self):
        expect, authentic = self.run.go_on_run(60)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_061_Web全球英语_前端排序条件总佣金降序(self):
        expect, authentic = self.run.go_on_run(61)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_062_Web全球英语_前端排序条件创建时间升序(self):
        expect, authentic = self.run.go_on_run(62)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_063_Web全球英语_前端排序条件创建时间降序(self):
        expect, authentic = self.run.go_on_run(63)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_064_Web全球英语_前端排序条件广告商_名称升序(self):
        expect, authentic = self.run.go_on_run(64)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_065_Web全球英语_前端排序条件广告商_广告数量降序(self):
        expect, authentic = self.run.go_on_run(65)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_066_Web全球英语_前端排序条件广告结束时间降序(self):
        expect, authentic = self.run.go_on_run(66)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_067_Web全球英语_前端排序条件产品一价格升序(self):
        expect, authentic = self.run.go_on_run(67)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_068_Web全球英语_前端排序条件产品一价格降序(self):
        expect, authentic = self.run.go_on_run(68)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_069_Web全球英语_前端排序条件产品_折扣升序(self):
        expect, authentic = self.run.go_on_run(69)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

    def test_070_Web全球英语_前端排序条件产品_折扣降序(self):
        expect, authentic = self.run.go_on_run(70)
        self.assertIn(expect, authentic, '实际与期望结果不一致,测试不通过')

