# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/9 20:06
@Auth ： Zhang
@File ：index.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from time import sleep

from page.base_page import BasePage
from selenium.webdriver.common.by import By

from page.dictionaries import Dictionaries


class Index(BasePage):
    URL = "/index"
    sys_manage = (By.CSS_SELECTOR,
                  '#asideNav > ul > div.submenu-box > div:nth-child(1) > div > div > div > div')
    dictionaries = (By.CSS_SELECTOR,'#asideNav > ul > div.submenu-box > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > span')


    def go_to_dictionaries(self):
        self.open()
        self.click(self.find_element(*self.sys_manage))
        self.click(self.find_element(*self.dictionaries))
        return Dictionaries(self._driver)

