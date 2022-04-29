from .base_page import BasePage

class HomePage(BasePage):
    def user_is_logged_in(self):
        current_page = self.driver.current_url
        assert "Home/Homepage" in current_page, "User is not logged in"


