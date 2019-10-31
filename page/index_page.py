"""首页页面"""
import unittest

from selenium.webdriver.common.by import By
from utils import DriverUtil

from base.base_page import BasePage, BaseHandle
from base.base_page import BasePage


class IndexPage(BasePage):
    """首页对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象
        self.login_link = (By.LINK_TEXT, "登录")
        self.search_bar = (By.ID, 'q')  # 搜索框
        self.ser_btn = (By.CLASS_NAME, 'ecsc-search-button')  # 搜索按钮

    def find_search_bar(self):  # 获取搜索框
        return self.find_element_func(self.search_bar)

    def find_ser_btn(self):
        return self.find_element_func(self.ser_btn)
        # 获取搜索按钮

    def find_login_link(self):
        """登录链接定位方法"""
        return self.find_element_func(self.login_link)


class IndexHandle(BaseHandle):
    """首页操作库层"""

    def __init__(self):
        self.index_page = IndexPage()  # 元素定位对象

    def click_login_link(self):
        """登录链接点击方法"""
        self.index_page.find_login_link().click()

    def input_search_bar(self, kw):
        """搜索框输入方法"""
        self.input_text(self.index_page.find_element_func(), kw)

    def click_ser_btn(self):
        """搜索按钮点击方法"""
        self.index_page.find_ser_btn().click()


class IndexProxy(object):
    """首页业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()  # 操作对象

    def go_to_login(self):
        """跳转登录页面方法"""
        self.index_handle.click_login_link()

    def search_goods(self, kw):
        self.index_handle.input_search_bar  # 输入关键字
        self.index_handle.click_ser_btn()  # 点击搜索按钮


if __name__ == '__main__':
    unittest.main()
