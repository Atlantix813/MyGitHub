from console.crm.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from helper.AppProxy import AppProxy

class OrderPage(BasePage):
    _request_url ="/index.php?g=CrmCommon&m=Order&a=applyOrderIframe&customer_id=" + AppProxy.getConfg("crm", "customer_id")

    # 用户姓名
    _customer_name_loc = (By.NAME, "customer_name")

    # 用户微信
    _customer_wechat_loc = (By.NAME, "customer_wechat")

    # 用户QQ
    _customer_qq_loc = (By.NAME, "customer_qq")

    # 用户性别
    _customer_sex_loc = (By.CSS_SELECTOR, "sex_man")

    # 用户年龄
    _customer_age_loc = (By.NAME, "customer_age")

    # 资金量
    _customer_fund_amount_loc = (By.NAME, "customer_fund_amount")

    # 用户地址
    _customer_address_loc = (By.NAME, "customer_address")

    # 营销总监确认
    _director_name_loc = (By.NAME, "director_name")

    # 营销经理确认
    _manager_name_loc = (By.NAME, "manager_name")

    # 营销顾问确认
    _salesman_name_loc = (By.NAME, "salesman_name")

    # 申请类型
    _apply_type_loc = (By.NAME, "apply_type")

    # 选择套餐
    _package_id_loc = (By.NAME, "package_id")

    # 订单缴费状态
    _order_check_status_loc = (By.NAME, "order_check_status")

    # 订单金额
    _order_fee_loc = (By.NAME, "order_fee")

    # 开始服务时间
    _start_serve_time_loc = (By.NAME, "start_serve_time")

    # 结束服务时间
    _end_serve_time_loc = (By.NAME, "end_serve_time")

    # 到账时间
    _account_time_loc = (By.NAME, "account_time")

    # 到账银行框
    _receipt_bank_loc = (By.NAME, "receipt_bank")

    # 到账银行打钩
    _account_select_loc = (By.XPATH, "/html/body/div[1]/form/table/tbody/tr[9]/td/div/label[9]/div/ul/li[1]/label/input")

    # 已缴订金
    _is_subscription_loc = (By.NAME, "is_subscription")

    # 是否立即开通服务
    _is_promptly_dredge_loc = (By.NAME, "is_promptly_dredge")

    # 转款人是否为客户本人
    _payer_is_self_loc = (By.NAME, "payer_is_self")

    # 凤凰资源
    _is_phoenix_resource_loc = (By.NAME, "is_phoenix_resource")

    # 缴费原因
    _pay_reason_2_loc = (By.NAME, "pay_reason_2")

    # 客户性格
    _customer_nature_2_loc = (By.NAME, "customer_nature_2")

    # 沟通方案-其他
    _talk_plan_0_loc = (By.NAME, "talk_plan_0")

    # 沟通方案-其他-文字输入框
    _other_talk_plan_loc = (By.NAME, "other_talk_plan")

    # 客户职业特征
    _customer_profession_loc = (By.NAME, "customer_profession")

    # 同步用户编号按钮
    _user_number_loc = (By.NAME, "user_number")

    # 职业
    _profession_loc = (By.NAME, "profession")

    # 入市时间
    _into_stock_time_loc = (By.NAME, "into_stock_time")

    # 入市盈利
    _into_stock_profit_loc = (By.NAME, "into_stock_profit")

    # 投资风格
    _investment_style_loc = (By.NAME, "investment_style")

    # 专业指导
    _is_guide_loc = (By.NAME, "is_guide")

    # 服务模式
    _serve_model_loc = (By.NAME, "serve_model")

    # 操作风格
    _operator_style_loc = (By.NAME, "operator_style")

    # 投资策略
    _investment_strategy_loc = (By.NAME, "investment_strategy")

    # 服务安排
    _serve_plan_loc = (By.NAME, "serve_plan")

    # 投顾团队
    _invest_consultant_team_id_loc = (By.NAME, "invest_consultant_team_id")

    # 提交按钮
    _post_submit_loc = (By.XPATH, "/html/body/div[1]/form/div/span[1]")

    '''
    单选框radio选择
    '''
    def clickradio(self,radios,num):
        radio = radios[num]
        radio.click()

