import pytest
import random

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.teams_page import TeamsPage

base_url = "http://10.94.6.100:50000"
site_id = "1002"
department_id = "1014"

team_name_when_creating = "KateTesterTeam" + str(random.randrange(1,1000))
new_team_name = team_name_when_creating + str(random.randrange(1,1000))
team_color_when_creating = "#" + ("%06x" % random.randint(0, 0xFFFFFF)).upper()
new_team_color = "#000000"

class TestUserCreatesNewTeam():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.link = base_url + "/Login"
        self.page = LoginPage(driver, self.link)
        self.page.open()
        self.page.login_user()
        self.page = HomePage(driver, driver.current_url)
        self.page.user_is_logged_in()
        self.page.remove_banner()
    
    #@pytest.mark.new
    def test_user_creates_teams(self, driver):
        self.link = base_url + "/ones/new?siteId=" + site_id + "&departmentIds=" + department_id
        self.page = TeamsPage(driver, self.link)
        self.page.open()
        self.page.user_selects_teams_tab()
        self.page.user_opens_team_creation_pop_up()
        self.page.user_changes_team_name(team_name_when_creating)
        self.page.user_changes_team_color(team_color_when_creating)
        self.page.user_saves_changes_in_team()
        self.page.check_if_create_team_notification_is_displayed()
        self.page.check_if_team_exists(team_name_when_creating)

    #@pytest.mark.new
    def test_user_edits_team(self, driver):
        self.link = base_url + "/ones/new?siteId=" + site_id + "&departmentIds=" + department_id
        self.page = TeamsPage(driver, self.link)
        self.page.open()    
        self.page.user_selects_teams_tab() 
        self.page.user_opens_team_to_edit(team_name_when_creating) 
        self.page.user_changes_team_name(new_team_name)
        self.page.user_changes_team_color(new_team_color)
        self.page.user_closes_team_editing_form()
        self.page.check_if_team_exists(new_team_name)

    @pytest.mark.new
    def test_user_deletes_team(self, driver):
        self.link = base_url + "/ones/new?siteId=" + site_id + "&departmentIds=" + department_id
        self.page = TeamsPage(driver, self.link)
        self.page.open()      
        self.page.user_selects_teams_tab() 
        self.page.user_opens_team_to_edit(new_team_name)
        self.page.user_deletes_team()
        self.page.check_if_remove_team_notification_is_displayed()
        self.page.check_if_team_not_exists(new_team_name)

        







