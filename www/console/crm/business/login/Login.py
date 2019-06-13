import unittest
from helper.AppProxy import AppProxy
from helper import helper
from console.crm.pages.login.LoginPage import LoginPage
from console.crm.pages.index.IndexPage import IndexPage
from console.crm.pages.index.ErrorPage import ErrorPage


"""
登录页面测试业务
"""
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = helper.genWebdriver()

    def tearDown(self):
        self.driver.quit()


    """
    正常登录
    """
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        # login_page.input_username(
        #     AppProxy.getConfg("crm", "username")
        # )
        # login_page.input_password(
        #     AppProxy.getConfg("crm", "password")
        # )
        #
        # # 提交
        # login_page.click_submit()

        """
        上面注释的代码其实已经封装在loginpage.py里面，可直接调用login()
        """
        login_page.login()

        index_page = IndexPage(self.driver)

        self.assertTrue(index_page.isUserInfoName("管理员admin"))


    """
    密码错误
    """
    def test_password_err_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_page.input_username(
            AppProxy.getConfg("crm", "username")
        )
        login_page.input_password(
            helper.genRandomeStr()
        )

        # 提交
        login_page.click_submit()

        error_page = ErrorPage(self.driver)

        self.assertTrue(error_page.isErrorInfo("密码错误！"))

    """
    用户名错误
    """
    def test_username_err_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_page.input_username(
            helper.genRandomeStr()
        )
        login_page.input_password(
            helper.genRandomeStr()
        )

        # 提交
        login_page.click_submit()

        error_page = ErrorPage(self.driver)

        self.assertTrue(error_page.isErrorInfo("用户名不存在！"))



