# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/7 23:29
@Auth ： Zhang
@File ：login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.index import Index


class Login(BasePage):
    URL = "/login"
    userName = (By.XPATH, '//*[@placeholder="请输入账号"]')
    passWord = (By.XPATH, '//*[@placeholder="请输入密码"]')
    submit = (By.CSS_SELECTOR, '.mt60 >  .el-button--default')

    # 去登录
    def go_to_login(self, userName, passWord):
        self.open()
        self.send_keys(self.find_element(*self.userName), userName)
        self.send_keys(self.find_element(*self.passWord), passWord)
        self.click(self.find_element(*self.submit))
        return Index(self._driver)


if __name__ == '__main__':
    login = Login()
    login.go_to_login()
