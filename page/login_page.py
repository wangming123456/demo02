"""登录界面"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()  # 获取父类浏览器对象

        self.username = (By.ID, 'username')  # 用户名
        self.password = (By.ID, 'password')  # 密码
        self.verify_code = (By.ID, 'verify_code')  # 验证码
        self.login_btn = (By.NAME, 'sbtbutton')  # 登录按钮

    def find_username(self):
        """用户名定位方法"""
        return self.find_element_func(self.username)

    def find_password(self):
        """密码定位方法"""
        return self.find_element_func(self.password)

    def find_verify_code(self):
        """验证码定位方法"""
        return self.find_element_func(self.verify_code)

    def find_login_btn(self):
        """登录按钮定位方法"""
        return self.find_element_func(self.login_btn)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()  # 获取元素定位对象

    def input_username(self, name):
        """用户名输入方法"""
        # self.login_page.find_username().clear()  # 输入框元素应该先执行清空操作, 再执行输入操作!
        # self.login_page.find_username().send_keys(name)
        self.input_text(self.login_page.find_username(), name)

    def input_password(self, pwd):
        """密码输入方法"""

        self.input_text(self.login_page.find_password(), pwd)

    def input_verify_code(self, code):
        """验证码输入方法"""

        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        """登录按钮点击方法"""
        self.login_page.find_login_btn().click()


class LoginProxy(object):
    def __init__(self):
        self.login_handle = LoginHandle()  # 操作对象

    def login(self, name, pwd, code):
        """登录方法"""
        self.login_handle.input_username(name)  # 输入用户名
        self.login_handle.input_password(pwd)  # 输入密码
        self.login_handle.input_verify_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录按钮

