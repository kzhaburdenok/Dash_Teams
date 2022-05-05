from asyncore import close_all
from string import digits
import time
import random
from turtle import color
from .base_page import BasePage
from .locators import TeamsPageLocators
from selenium.webdriver.common.by import By



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

    def user_changes_team_name(self, team_name):
        self.driver.find_element(*TeamsPageLocators.TEAM_NAME_ICON).click()
        free_team_name_switcher = self.driver.find_element(*TeamsPageLocators.FREE_NAMES_SWITCHER)
        team_name_input_field = self.driver.find_element(*TeamsPageLocators.TEAM_NAME_INPUT)        
        if team_name_input_field.get_attribute("disabled") == "true":
            free_team_name_switcher.click()
            time.sleep(3)
        team_name_input_field.click()
        team_name_input_field.clear()
        team_name_input_field.send_keys(team_name)
        time.sleep(3)        
        confirm_team_name_btn = self.driver.find_element(*TeamsPageLocators.CONFIRM_TEAM_NAME_BTN)
        confirm_team_name_btn.click()
        time.sleep(3)
                
        displayed_team_name = self.driver.find_element(*TeamsPageLocators.TEAM_NAME_FIELD).text
        
        assert displayed_team_name == team_name, "Another name is entered"

    def user_changes_team_color(self,team_color):
        self.driver.find_element(*TeamsPageLocators.COLOR_PICKER).click()
        color_picker_value = self.driver.find_element(*TeamsPageLocators.COLOR_PICKER_INPUT_FIELD)
        time.sleep(3)
        color_picker_value.click()
        color_picker_value.clear()
        color_picker_value.send_keys(team_color)
        self.driver.find_element(*TeamsPageLocators.CONFIRM_PICKER_BTN).click()
        time.sleep(3)
        entered_color = self.driver.find_element(*TeamsPageLocators.SET_PICKER_COLOR).text
        assert entered_color == team_color, f"Color '{team_color}' is expected, but color '{entered_color}' is selected"

    def user_saves_changes_in_team(self):
        self.driver.find_element(*TeamsPageLocators.CONFIRM_CHANGE_IN_TEAM).click()
        time.sleep(3)

    def check_if_create_team_notification_is_displayed(self):
        assert self.is_element_present(*TeamsPageLocators.NOTIFICATION_TEAM_CREATED), "Notification is not displayed"

    def check_if_remove_team_notification_is_displayed(self):
        time.sleep(3)
        assert self.is_element_present(*TeamsPageLocators.NOTIFICATION_TEAM_REMOVED), "Notification is not displayed"

    def check_if_team_exists(self, team_name):
        assert self.is_element_present(By.XPATH, f"//div[contains(text(), '{team_name}')]"), "Team is not created"

    def check_if_team_not_exists(self, team_name):
        assert self.is_not_element_present(By.XPATH, f"//div[contains(text(), '{team_name}')]"), "Team is not created"

    def user_opens_team_to_edit(self, team_name):
        self.driver.find_element(By.XPATH, f"//div[@class='team']/descendant::div[contains(text(), '{team_name}')]/following::span[contains(@class, 'controls__btn_edit')]").click()
        time.sleep(5)
    
    def user_closes_team_editing_form(self):
        close_button = self.driver.find_element(*TeamsPageLocators.CLOSE_TEAMS_EDITING_FORM)
        close_button.click()

    def user_deletes_team(self):
        self.driver.find_element(*TeamsPageLocators.DELETE_TEAM_BTN).click()
        self.driver.find_element(*TeamsPageLocators.CONFIRM_DELETING_BTN).click()



