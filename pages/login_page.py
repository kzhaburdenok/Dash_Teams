from .base_page import BasePage
from .locators import LoginPageLocators

username_value = "global"
password_value = "global"

class LoginPage(BasePage):
    def login_user(self):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username_value)
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password_value)
        self.driver.find_element(*LoginPageLocators.REMEMBER_ME).click()
        self.driver.find_element(*LoginPageLocators.LOG_IN_BTN).click()
