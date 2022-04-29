import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.teams_page import TeamsPage

base_url = "http://10.94.6.100:50000"
site_id = "1002"
department_id = "1014"

class TestUserCreatesNewTeam():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.link = base_url + "/Login"
        self.page = LoginPage(driver, self.link)
        self.page.open()
        self.page.login_user()
        self.page = HomePage(driver, driver.current_url)
        self.page.user_is_logged_in()
        self.page.close_banner()

    def test_user_creates_teams(self, driver):
        self.link = base_url + "/ones/new?siteId=" + site_id + "&departmentIds=" + department_id
        print("my link is: ", self.link)
        self.page = TeamsPage(driver, self.link)
        self.page.open()
        self.page.user_opens_create_new_team_form()

        







