import unittest
from helper.AppProxy import AppProxy
from helper import helper
from console.crm.pages.knowledge.CategoryStorePage import CategoryStorePage
from console.crm.pages.login.LoginPage import LoginPage
from console.crm.pages.knowledge.CategoryIndexPage import CategoryIndexPage



"""
登录页面测试业务
"""
class Category(unittest.TestCase):
    def setUp(self):
        self.driver = helper.genWebdriver()

    def tearDown(self):
        self.driver.quit()

    """
    正常添加分类
    """
    def test_store_category(self):
        login_page = LoginPage(self.driver)
        category_store = CategoryStorePage(self.driver)
        category_index = CategoryIndexPage(self.driver)

        # 登录
        login_page.open()
        login_page.login()

        # 输入数据
        name = helper.genRandomeStr(10)
        value = "88"
        category_store.open()
        category_store.select_pid(value)
        category_store.input_name(name)
        category_store.input_remark(helper.genRandomeStr(10))


        # 提交数据
        category_store.click_submit()


        # 打开分类列表页
        category_index.open()
        self.assertTrue(category_index.checkName(name))
