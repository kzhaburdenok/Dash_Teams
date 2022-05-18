import pytest
import random
import requests

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

    def test_create_team_by_api(setup):
        response = requests.get(base_url + "/ones/new?siteId=" + site_id + "&departmentIds=" + department_id)
        print ("response is:\n ", response.json)