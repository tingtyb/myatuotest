from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        # if driver is None:
        #     self._driver = webdriver.Chrome()
        # else:
        self._driver = driver


