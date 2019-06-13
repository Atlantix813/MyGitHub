from helper.AppProxy import AppProxy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" 
基础页面类 

# 注意！！！ node.text 只会展示显示的数据，即被遮挡的内容是读取不了的
# 最好使用 element.get_attribute("innerText") 来获取内容
"""
class BasePage(object):
    _request_url = ""

    def __init__(self, driver):
        self.driver   = driver
        self.base_url = "/".join((
            AppProxy.getConfg("crm", "base_url").strip("/"),
            self._request_url
        ))

    def _open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def open(self):
        self._open(self.base_url)

    """
    查找对应的元素,单个
    """
    def must_find_element(self, *loc):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc)
        )

    """
    查找所有的元素,集合
    """
    def must_find_all_element(self, *loc):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(loc)
        )

    """
    检测表示是否对应
    """
    def checkTitle(self, title):
        return WebDriverWait(self.driver, 5).until(
            EC.title_is(title)
        )

