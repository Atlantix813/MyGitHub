from console.crm.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

"""
登录的主框架页面
"""
class IndexPage(BasePage):
    _request_url  = "/index.php?g=&m=Index&a=index"

    _user_info_name_loc = (By.CSS_SELECTOR, '#sidebar .user-info')

    def isUserInfoName(self, name):
        return self.must_find_element(*self._user_info_name_loc).text.strip() == name
