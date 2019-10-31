"""
PO 文件的基类
"""
from utils import DriverUtil


class BasePage(object):
    """对象库层-基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def find_element_func(self, location):
        """元素定位方法"""
        # return self.driver.find_element(self.username[0], self.username[1])
        return self.driver.find_element(location[0], location[1])


class BaseHandle(object):
    """操作层-基类"""
    def input_text(self, element, text):
        """输入内容方法"""
        # self.login_page.find_username().clear()
        # self.login_page.find_username().send_keys(text)
        element.clear()
        element.send_keys(text)
