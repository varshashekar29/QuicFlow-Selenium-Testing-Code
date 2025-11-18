import pytest
from selenium import webdriver
from helpers.login_helper import perform_login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    perform_login(driver)
    return driver
    
