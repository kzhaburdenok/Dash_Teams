import time
from .base_page import BasePage
from .locators import TeamsPageLocators


class TeamsPage(BasePage):
    def user_opens_create_new_team_form(self):
        print("I'm trying to open teams page")
        if self.is_not_element_present(*TeamsPageLocators.TEAMS_TAB_ACTIVE):
            self.driver.find_element(*TeamsPageLocators.TEAMS_TAB).click()
            time.sleep(5)
        assert self.is_element_present(*TeamsPageLocators.SEARCH_TEAM_FIELD), "Teams tab is not clicked"