from selenium.webdriver.common.by import By
from page.basepage import BasePage
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.to_baidu import ToBaidu1


class Testone:

    def test_one(self):
        a=None
        # assert a is not None
        assert ToBaidu1().to_baidu1() is not None

    def tear_down(self):
        ToBaidu1()._driver.quit()


