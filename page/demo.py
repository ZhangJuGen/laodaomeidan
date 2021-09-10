# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/9 21:08
@Auth ： Zhang
@File ：demo.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium import  webdriver
from selenium.webdriver.common.by import By
dictionaries = (By.CSS_SELECTOR,
                    '# asideNav > ul > div.submenu-box > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) '
                    '> span ')
driver=webdriver.Chrome()
driver.get()
driver.find_element(dictionaries)