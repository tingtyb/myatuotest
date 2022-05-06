from selenium.webdriver.common.by import By
from page.basepage import BasePage
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class ToBaidu1(BasePage):
    _base_url = "https://www.baidu.com"

    def to_baidu1(self):
        self._driver.get(self._base_url)
        self._driver.maximize_window()
        sleep(5)
        self._driver.find_element(By.ID, 'kw').send_keys('haha')
        self._driver.find_element(By.ID, 'su').click()
        sleep(3)
        return None

