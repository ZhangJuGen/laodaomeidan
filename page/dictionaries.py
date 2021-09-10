# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/9 20:48
@Auth ： Zhang
@File ：dictionaries.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Dictionaries(BasePage):
    add = (By.CSS_SELECTOR,
           '#loyout > section > main > section > div > section > main > div > main > div > div.clearfix >'
           ' div:nth-child(2) > div > button')
    doctor=(By.CSS_SELECTOR,
            '#loyout > section > main > section > div > section > main > div > main > div '
            '> div.el-dialog__wrapper > div > div.el-dialog__body > form > div.el-form-item.is-required '
            '> div > div > input')
    def add_dictionaries(self):
        self.click(self.find_element(*self.add))
        self.send_keys(self.find_element(*self.doctor),'123456')
