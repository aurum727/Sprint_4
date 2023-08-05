import pytest
from selenium import webdriver
from locators.main_page_locators import MainPageLocators

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
