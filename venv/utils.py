"""
公共方法
"""
import time

from selenium import webdriver


def get_tips_message():
    """获取弹窗消息方法"""
    # msg = self.driver.find_element_by_class_name('layui-layer-content').text
    # driver = webdriver.Chrome()
    driver = DriverUtil.get_driver()  # 获取浏览器对象
    msg = driver.find_element_by_class_name('layui-layer-content').text
    print('msg=', msg)
    return msg


class DriverUtil(object):
    """浏览器工具类"""
    driver = None  # 为了表示浏览器对象的初始化状态(判断条件无法表示对象状态)

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了保证获取的浏览器对象始终是同一个, 需要条件判断浏览器对象的状态
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
            cls.driver.get('http://127.0.0.1/')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 需要判断浏览器对象存在再执行退出操作
        # if cls.driver is not None:
        if cls.driver:
            cls.driver.quit()
            cls.driver = None  # 保险措施, 确保浏览器对象的初始化状态


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(2)
    DriverUtil.quit_driver()
