from cement import Controller, ex
import unittest
from helper import helper

class CrmController(Controller):

    """基础模块，给予其它模块继承所用"""

    """产品统计"""
    class Meta:
        label = 'crm'
        stacked_on = 'base'
        stacked_type = 'nested' # embedded
        description = "呼叫系统"

    @ex(
        help="呼叫系统单元测试",
        arguments=[
            (
                ['-p', '--path'],
                {
                    'help' : '外部传入的测试路径',
                }
            )
        ]
    )
    def test(self):
        runner = unittest.TextTestRunner()

        # 外部传入的测试路径
        if self.app.pargs.path is not None :
            runner.run(
                unittest.TestLoader().discover(helper.getHome(self.app.pargs.path), pattern="*.py")
            )
        else:
            runner.run(
                helper.loadTestDiscover("console/crm/business")
            )
