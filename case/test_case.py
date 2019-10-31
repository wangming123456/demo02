from utils import DriverUtil, get_tips_message
import unittest
from time import sleep

from page.index_page import IndexProxy
from page.login_page import LoginProxy


class TestTPShopLogin(unittest.TestCase):
    """TPShop 测试类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy() #获取首页界面
        cls.login_proxy = LoginProxy()  # 获取登录页面业务执行对象

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self):
        self.driver.get('http://127.0.0.1/')  # 跳转首页
        # 点击首页的‘登录’链接，进入登录页面
        self.index_proxy.go_to_login()

    def test_login(self):
        self.login_proxy.login("17621836183", "zhanglin0724", "8888")
        sleep(10)
        title = self.driver.title
        self.assertIn('我的账户', title)


if __name__ == '__main__':
    unittest.main()
