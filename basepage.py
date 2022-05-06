from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            print('我用到了if')
        else:
            self._driver = driver
            print('我用到了else')
        if self._base_url != '':
            self._driver.get(self._base_url)


