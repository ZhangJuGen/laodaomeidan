# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/9 20:10
@Auth ： Zhang
@File ：test_01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import unittest

from page import index
from page.index import Index
from page.login import Login
from selenium.webdriver.common.by import By

class Test_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.userName = 'csgly'
        cls.passWord = '123456'

    def setUp(self):
        self.login=Login()
        self.index=Index()
    def test_1login(self):
        self.login.go_to_login(self.userName,self.passWord)

    @unittest.skip
    def test_2add_dictionaries(self):
        self.index.go_to_dictionaries().add_dictionaries()
