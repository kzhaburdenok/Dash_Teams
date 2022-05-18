from selenium.webdriver import Remote as RemoteWebDriver # импортим ремоут вебдрайвер
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.locators import BasePageLocators

class BasePage():
    def __init__(self, driver: RemoteWebDriver, url, timeout = 5):
    #def __init__(self, driver, url, timeout = 5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self, timeout = 5):
        self.driver.get(self.url)
        self.driver.implicitly_wait(timeout)
    
    def remove_banner(self):
        time.sleep(5)
        self.driver.find_element(*BasePageLocators.BANNER_CLOSE_ICON).click()
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout = 5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False
