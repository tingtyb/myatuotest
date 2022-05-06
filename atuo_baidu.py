from selenium.webdriver.common.by import By
from basepage import BasePage
from time import sleep


class Tobaidu(BasePage):
    def tobaidu(self):

        self._driver.get("https://www.baidu.com")
        self._driver.maximize_window()
        sleep(5)
        self._driver.find_element(By.ID, 'kw').send_keys('haha')
        self._driver.find_element(By.ID, 'su').click()
        sleep(3)
        self._driver.close()


Tobaidu().tobaidu()