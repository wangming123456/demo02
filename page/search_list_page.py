"""
列表搜索界面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class SearchListPage(BasePage):
    """搜索列表界面对象库层"""
    def __init__(self):
        super().__init__()
        self.search_goods = (By.XPATH,'//*[@class="shop_name2"]/*[contains(text(),"{}")]')

    def find_search_goods(self, kw):
        location = (self.search_goods[0],self.search_goods[1])
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """搜索列表界面操作层"""
    def __init__(self):
        self.search_list_page = SearchListPage()

    def click_search_goods(self, kw):
        """搜索到的商品点击方法"""
        self.search_list_page.find_search_goods(kw).click()


class SearchListProxy(object):
    def __init__(self):
        self.search_list_handle = SearchListHandle()

    def go_to_goods_deatil(self, kw):
        """跳转商品详情页"""
        self.search_list_handle.click_search_goods(kw)
