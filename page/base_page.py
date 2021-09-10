# -*- coding: utf-8 -*-
"""
Page Object设计模式和原则:
1.一个 public 方法代表一个公共的服务。就是说一个方法代替页面上的某个操作
2.PageObject 中的方法细节不可暴露在外，通过提供公共服务接口的形式提供给外部
3.一般不需要在 PageObject 中断言
4.当有页面跳转的操作时候，执行这个方法时应该在方法结束返回时能够跳转到另一个页面中
5.我们只需要对页面中我们需要的重要的内容进行封装
6.页面中相同的组件，但是不同的操作应该要被拆成不同的方法进行封装

"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BasePage_Config


class BasePage:
    """
    构造函数:如果继承时传递了driver，则使用传递过来的driver，否则复用浏览器
    复用命令：chrome --remote-debugging-port=9222
    """
    URL=BasePage_Config.URL

    def __init__(self, driver: WebDriver = None):
        self.host=BasePage_Config.HOST
        self.time_out = BasePage_Config.TIMEOUT
        if None == driver:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(self.time_out)

        else:
            self._driver = driver

    """
    初始化等待时间，方便其他方法调用
    """
    def init_wait(self,timeout=None):
        if None == timeout:
            timeout=BasePage_Config.TIMEOUT
        return WebDriverWait(driver=self._driver,timeout=timeout)

    """
    定位单个元素，系统报错时会退出浏览器并提示定位方式
    """
    def find_element(self, *locator, timeout=None):
        try:
            self.init_wait(timeout).until(EC.presence_of_element_located(locator))
        except(NoSuchElementException,TimeoutException):
            self.quite()
            raise TimeoutException(msg="定位元素失败，定位方式为{}".format(locator))
        return self._driver.find_element(*locator)

    """
        定位多个元素，系统报错时会退出浏览器并提示定位方式
    """
    def find_elements(self, *locator, timeout=None):
        try:
            self.init_wait(timeout).until(EC.presence_of_all_elements_located(locator))
        except(NoSuchElementException, TimeoutException):
            self.quite()
            raise TimeoutException(msg="定位元素失败，定位方式为{}".format(locator))
        return self._driver.find_elements(*locator)

    """
    输入
    """
    def send_keys(self,webElement,keys):
        webElement.clear()
        webElement.send_keys(keys)

    """
    点击
    """
    def click(self,webElement):
        webElement.click()

    """
    打开浏览器
    """
    def open(self):
        self._driver.get(self.host+self.URL)

    """
    关闭当前标签页
    """
    def close(self):
        self._driver.close()

    """
    退出浏览器
    """
    def quite(self):
        self._driver.quit()




