from string import digits
import time
import random
from turtle import color
from .base_page import BasePage
from .locators import TeamsPageLocators
from selenium.webdriver.common.by import By

team_name = "KateTesterTeam" + str(random.randrange(1,1000))
team_color_when_creating = "#" + ("%06x" % random.randint(0, 0xFFFFFF)).upper()
class TeamsPage(BasePage):
    def user_selects_teams_tab(self):
        if self.is_not_element_present(*TeamsPageLocators.TEAMS_TAB_ACTIVE):
            self.driver.find_element(*TeamsPageLocators.TEAMS_TAB).click()
            time.sleep(5)
        assert self.is_element_present(*TeamsPageLocators.SEARCH_TEAM_FIELD), "Teams tab is not clicked"

    def user_opens_team_creation_pop_up(self):
        self.driver.find_element(*TeamsPageLocators.CREATE_NEW_TEAM_BTN).click()
        time.sleep(5)
        assert self.is_element_present(*TeamsPageLocators.CREATE_TEAM_POPUP), "Create Team Pop Up is not displayed"

    def user_changes_team_name(self):
        self.driver.find_element(*TeamsPageLocators.TEAM_NAME_ICON).click()
        self.driver.find_element(*TeamsPageLocators.FREE_NAMES_SWITCHER).click()
        time.sleep(3)
        team_name_input_field = self.driver.find_element(*TeamsPageLocators.TEAM_NAME_INPUT)
        team_name_input_field.click()
        team_name_input_field.clear()
        team_name_input_field.send_keys(team_name)
        time.sleep(3)        
        confirm_team_name_btn = self.driver.find_element(*TeamsPageLocators.CONFIRM_TEAM_NAME_BTN)
        confirm_team_name_btn.click()
        time.sleep(3)
                
        displayed_team_name = self.driver.find_element(*TeamsPageLocators.TEAM_NAME_FIELD).text
        
        assert displayed_team_name == team_name, "Another name is entered"

    def user_changes_team_color(self):
        self.driver.find_element(*TeamsPageLocators.COLOR_PICKER).click()
        color_picker_value = self.driver.find_element(*TeamsPageLocators.COLOR_PICKER_INPUT_FIELD)
        time.sleep(3)
        color_picker_value.click()
        color_picker_value.clear()
        color_picker_value.send_keys(team_color_when_creating)
        self.driver.find_element(*TeamsPageLocators.CONFIRM_PICKER_BTN).click()
        time.sleep(3)
        entered_color = self.driver.find_element(*TeamsPageLocators.SET_PICKER_COLOR).text
        assert entered_color == team_color_when_creating, f"Color '{team_color_when_creating}' is expected, but color '{entered_color}' is selected"

    def user_saves_changes_in_team(self):
        self.driver.find_element(*TeamsPageLocators.CONFIRM_CHANGE_IN_TEAM).click()
        time.sleep(3)

    def check_if_notification_is_displayed(self):
        assert self.is_element_present(*TeamsPageLocators.NOTIFICATION_TEAM_CREATED), "Notification is not displayed"


    def check_if_team_exists(self):
        assert self.is_element_present(By.XPATH, f"//div[contains(text(), '{team_name}')]"), "Team is not created"


