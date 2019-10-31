"""
购物车测试用例
"""

import unittest

from utils import DriverUtil
from time import sleep

from page.goods_detail_page import GoodsDeatilProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from page.search_list_page import SearchListProxy


class TestTPShopCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.good_detail_proxy = GoodsDeatilProxy()#获取商品详情页面业务执行对象
        cls.search_list_proxy = SearchListProxy()  # 获取搜索列表界面业务执行对象
        cls.index_proxy = IndexProxy()  # 获取首页页面业务执行对象

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self):
        self.driver.get('http://127.0.0.1/')  # 跳转首页

    def test_cart(self):
        """购物车测试方法"""
        goods_name = "小米手机"
        self.index_proxy.search_goods(goods_name)#搜索商品
        self.search_list_proxy.go_to_goods_deatil(goods_name)#跳转商品详情界面
        self.good_detail_proxy.join_cart_func()#添加购物
        msg = self.good_detail_proxy.get_result()#获取添加结果
        #断言判断

        sleep(10)

        self.assertIn('添加成功', msg)


if __name__ == '__main__':
    unittest.main()
