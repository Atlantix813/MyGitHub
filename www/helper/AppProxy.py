
"""
 命令行对象代理，主要给测试用例调用
"""
class AppProxy(object):
    __app = None;

    """
    仅仅初始化一次，避免多次覆盖
    """
    @staticmethod
    def setApp(app):
        if AppProxy.__app == None:
            AppProxy.__app = app


    @staticmethod
    def getConfg(*args, **kwargs):
        return AppProxy.__app.config.get(*args, **kwargs)
