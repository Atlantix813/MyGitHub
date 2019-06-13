from console.crm.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CategoryStorePage(BasePage):
    _request_url  = "/index.php?g=Knowledge&m=Category&a=store"

    # 上级分类
    _pid_loc    = (By.NAME, "pid")
    # 分类名称
    _name_loc   = (By.NAME, "name")
    # 排序
    _sort_loc   = (By.NAME, "sort")
    # 备注
    _remark_loc = (By.NAME, "remark")
    # 保存
    _submit_btn_loc = (By.CSS_SELECTOR, '[type="submit"]')

    """
    :param pid option 的 value 值
    """
    def select_pid(self, pid):
        Select(
            self.must_find_element(*self._pid_loc)
        ).select_by_value(pid)

    def input_name(self, name):
        self.must_find_element(*self._name_loc).send_keys(name)

    def input_sort(self, sort):
        self.must_find_element(*self._sort_loc).send_keys(sort)

    def input_remark(self, remark):
        self.must_find_element(*self._remark_loc).send_keys(remark)

    def click_submit(self):
        self.must_find_element(*self._submit_btn_loc).click()
