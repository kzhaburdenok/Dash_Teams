import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver(request):
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    print("\nquit browser..")
    driver.quit()