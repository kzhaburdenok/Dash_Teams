from string import digits
import time
import random
from .base_page import BasePage
from .locators import TeamsPageLocators

team_name = "KateTesterTeam" + random.choice(digits)
class TeamsPage(BasePage):
    def user_selects_teams_tab(self):
        if self.is_not_element_present(*TeamsPageLocators.TEAMS_TAB_ACTIVE):
            self.driver.find_element(*TeamsPageLocators.TEAMS_TAB).click()
            time.sleep(5)
        assert self.is_element_present(*TeamsPageLocators.SEARCH_TEAM_FIELD), "Teams tab is not clicked"

    def user_creates_new_team(self):
        self.driver.find_element(*TeamsPageLocators.CREATE_NEW_TEAM_BTN).click()
        time.sleep(5)
        assert self.is_element_present(*TeamsPageLocators.CREATE_TEAM_POPUP), "Create Team Pop Up is not displayed"
