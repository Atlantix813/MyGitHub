from console.crm.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from helper.AppProxy import AppProxy
import time

class CategoryIndexPage(BasePage):
    _request_url  = "/index.php?g=Knowledge&m=Category&a=manage&menuid=" + AppProxy.getConfg("crm", "category_index_menuid")

    # 上级分类
    _name_tds = (By.CSS_SELECTOR, ".table_main tbody tr td:nth-of-type(2)")

    """
    :param pid option 的 value 值
    """
    def checkName(self, name):
        # 注意！！！ node.text 只会展示显示的数据，即被遮挡的内容是读取不了的
        for element in self.must_find_all_element(*self._name_tds):
            if name == element.get_attribute("innerText").strip().strip("|-- ") :
                return True


        return False
