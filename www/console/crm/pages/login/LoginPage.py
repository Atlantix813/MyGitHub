from console.crm.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from helper.AppProxy import AppProxy

class LoginPage(BasePage):
    _request_url  = "/"

    _username_loc = (By.ID, 'js-admin-name')
    _password_loc = (By.ID, 'admin_pwd')
    _submit_loc   = (By.NAME, 'submit')

    def input_username(self, username):
        self.must_find_element(*self._username_loc).send_keys(username)

    def input_password(self, password):
        self.must_find_element(*self._password_loc).send_keys(password)

    def click_submit(self):
        self.must_find_element(*self._submit_loc).click()


    """
    登录
    """
    def login(self):
        self.input_username(
            AppProxy.getConfg("crm", "username")
        )
        self.input_password(
            AppProxy.getConfg("crm", "password")
        )

        self.click_submit()

