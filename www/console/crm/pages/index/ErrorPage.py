from console.crm.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

"""
登录的主框架页面
"""
class ErrorPage(BasePage):
    # 错误页面没有具体链接
    _request_url  = ""

    _error_cont_loc = (By.CSS_SELECTOR, '#error_tips .error_cont li')

    def isErrorInfo(self, info):
        return self.must_find_element(*self._error_cont_loc).text.strip() == info
