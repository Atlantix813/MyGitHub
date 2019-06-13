from cement.core.foundation import App
from cement.core import hook
from helper import helper
from helper.AppProxy import AppProxy


from console.crm.base import CrmController



class StatisticsApp(App):
    class Meta:
        label = 'statistics'
        handlers = [
            CrmController,
        ]
        # @TODO 重点！！线上的日志文件一定要写全路径！！！
        config_files=[
            helper.getHome('config/override.conf'),
            helper.getHome('config/local.conf'), # 本地文件，已经添加到忽略文件中
            helper.getHome('config/product.conf'), # 此文件必须放在最后面作覆盖作用
        ]

with StatisticsApp() as app:

    # 模块初始化

    # 注册关闭时的回调
    # hook.register('pre_close', close.close)

    # 初始化 app 对象
    AppProxy.setApp(app)

    app.run()
