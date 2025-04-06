from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.config import Config
from src.pages.main_page import MainPage

def test_scooter_logo_redirects_home(driver):
    main_page = MainPage(driver)
    main_page.close_cookies()
    main_page.click_order_header()  # Navigate to the order form

    main_page.click_logo_scooter()  # Click the Samokat logo
    # Wait until the URL becomes the main page
    WebDriverWait(driver, 10).until(EC.url_to_be(Config.BASE_URL))

    # Assert that the current URL is the homepage URL
    assert driver.current_url == Config.BASE_URL


def test_yandex_logo_opens_dzen(driver):
    main_page = MainPage(driver)
    main_page.close_cookies()
    main_page.click_logo_yandex()

    # Switch to the newly opened window
    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 20).until(EC.url_to_be(Config.DZEN_URL))

    # Assert that the current URL is the Dzen redirect URL
    assert driver.current_url == Config.DZEN_URL
