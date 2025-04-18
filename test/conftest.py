# test/conftest.py
import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox()

    # Navigate to the base URL
    driver.get(Config.BASE_URL)

    # Provide the driver to the test
    yield driver

    # Quit the driver after the test
    driver.quit()
