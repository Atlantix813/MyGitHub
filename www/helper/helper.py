import os
import unittest
import random
from selenium import webdriver

# 用于保存 getHome 的常量
_global_path = ""

# 在有传入文件路径的情况下有把文件路径追加到后面
def getHome(file_path=None) :
    global _global_path
    if _global_path == "" :
        _global_path = os.path.dirname(os.path.realpath(__file__))
        _global_path = os.path.normpath(os.path.join(_global_path, "../"))

    if file_path is None:
        return _global_path

    # 整理正常的路径
    return os.path.normpath(
        os.path.join(_global_path, file_path)
    )


"""
    加载所有的单元测试用例
    @:param path 对应单元测试路径
"""
def loadTestDiscover(path):
    path = getHome(path)
    suites = []

    # 追加当前路径
    suites.append(unittest.TestLoader().discover(path))


    # 若是文件夹则遍历下面的所有文件夹
    if os.path.isdir(path) :
        list = os.listdir(path)
        for file in list :
            full_path = os.path.join(path, file)
            if os.path.isdir(full_path) and file != "__pycache__":
                suites.append(unittest.TestLoader().discover(full_path, pattern="*.py"))

    return unittest.TestSuite(suites)

"""
生成浏览器
"""
def genWebdriver():
    options = webdriver.ChromeOptions()
    # options.headless = True

    return webdriver.Chrome(options=options)

"""
生成指定长度的随机字符串
"""
def genRandomeStr(num = 5):
    return "".join(random.sample("abcdefghijklmnopqrstuvwxyz", num))
