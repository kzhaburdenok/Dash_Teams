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
    CREATE_TEAM_POPUP = (By.XPATH, "//div[@class='createTeamPopup']")
    TEAM_NAME_ICON = (By.XPATH, "//span[@class='inputGroup__icon']")
    FREE_NAMES_SWITCHER = (By.XPATH, "//span[@class='vueSlider round']")
    TEAM_NAME_INPUT = (By.XPATH, "//div[@class='team__input']/child::input[@maxlength='30']")
    CONFIRM_TEAM_NAME_BTN = (By.XPATH, "//div[contains(@class, 'buttons__btn_submit')]")
    TEAM_NAME_FIELD = (By.XPATH, "//div[contains(@class,'inputGroup_name')]/child::div[contains(@class, 'inputGroup__input')]")
    COLOR_PICKER = (By.XPATH, "//div[contains(@class, 'inputGroup__picker')]")
    COLOR_PICKER_INPUT_FIELD = (By.XPATH, "//div[contains(@class, 'teamTab__color')]/descendant::input[contains(@class, 'cp-input__input')]")
    CONFIRM_PICKER_BTN = (By.XPATH, "//div[contains(@class, 'picker__btn_confirm')]")
    SET_PICKER_COLOR = (By.XPATH, "//div[contains(@class, 'toggle__label')]")
    CONFIRM_CHANGE_IN_TEAM = (By.XPATH, "//div[contains(@class, 'controls__btn_transfer')]")
    NOTIFICATION_TEAM_CREATED = (By.XPATH, "//div[contains(text(), 'Team created')]")
    NOTIFICATION_TEAM_REMOVED = (By.XPATH, "//div[contains(text(), 'Team removed')]")    
    CLOSE_TEAMS_EDITING_FORM = (By.XPATH, "//div[contains(@class, 'controls__btn_close')]/child::button")
    DELETE_TEAM_BTN = (By.XPATH, "//div[contains(@class, 'controls__btn_delete')]/child::button")
    CONFIRM_DELETING_BTN = (By.XPATH, "//div[contains(@class, 'btn_submit')]")
    