from selenium.webdriver.common.by import By

class BasePageLocators():
    BANNER_CLOSE_ICON = (By.XPATH, "//span[@class='header-banner__close-button']")

class LoginPageLocators():
    USERNAME = (By.NAME, "UserName")
    PASSWORD = (By.NAME, "Password")
    REMEMBER_ME = (By.NAME, "RememberMe")
    LOG_IN_BTN = (By.XPATH, "//button[@type = 'submit']")

class TeamsPageLocators():
    TEAMS_TAB = (By.XPATH, "//li[contains(@class, 'VTab__btn_teams')]/child::span")
    TEAMS_TAB_ACTIVE = (By.XPATH, "//li[contains(@class, 'VTab__btn_teams VTab__btn_active')]")
    CREATE_NEW_TEAM_BTN = (By.XPATH, "//div[contains(@class, 'TeamsTab__create')]/descendant::span[@class='VButton__text']")
    SEARCH_TEAM_FIELD = (By.XPATH, "//input[@placeholder='Search Teams']")
    TEAM_NAME = (By.XPATH, "//div[contains(@class,'inputGroup_name')]/child::div[contains(@class, 'inputGroup__input')]")
    CREATE_TEAM_POPUP = (By.XPATH, "//div[@class='createTeamPopup']")
    
