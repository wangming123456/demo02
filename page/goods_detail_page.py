"""
商品详情界面
"""
from selenium.webdriver.common.by import By
from utils import DriverUtil

from base.base_page import BasePage, BaseHandle


class GoodsDeatilPage(BasePage):
    """商品详情-对象库层"""

    def __init__(self):
        super(GoodsDeatilPage, self).__init__()
        self.join_cart_btn = (By.ID, 'join_cart')
        self.join_result = (By.CSS_SELECTOR, '.conect-title')

    def find_join_cart_btn(self):
        """加入购物车按钮定位方法"""
        return self.find_element_func(self.find_join_cart_btn())

    def find_join_result(self):
        """加入购物车定位方法"""
        return self.find_element_func(self.join_result)


class GoodsDeatilHandle(BaseHandle):
    def __init__(self):
        self.goods_deatil_page = GoodsDeatilPage()

    def click_join_cart_btn(self):
        self.goods_deatil_page.find_join_cart_btn().click()

    def get_join_result(self):
        """添加购物车结果方法获取"""
        driver = DriverUtil.get_driver()
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        return self.goods_deatil_page.find_join_result().text


class GoodsDeatilProxy(object):
    def __init__(self):
        self.goods_deatil_handle = GoodsDeatilHandle()

    def join_cart_func(self):
        self.goods_deatil_handle.click_join_cart_btn()

    def get_result(self):
        return self.goods_deatil_handle.get_join_result()
