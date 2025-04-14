from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from src.pages.locators import OrderPageLocators



class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_customer_info(self, first_name: str, last_name: str, address: str, metro: str, phone: str):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.lastname_input).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(address)

        self.driver.find_element(*OrderPageLocators.subway_input).click()
        station_locator = (By.XPATH, OrderPageLocators.station_menu_item % metro)
        station_menu = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(station_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", station_menu)
        station_menu.click()

        self.driver.find_element(*OrderPageLocators.phone_input).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    def fill_rent_info(self, rent_date: str):
        self.driver.find_element(*OrderPageLocators.date_input).send_keys(rent_date, Keys.ENTER)
        self.driver.find_element(*OrderPageLocators.rent_period_input).click()
        self.driver.find_element(*OrderPageLocators.rent_period_menu_item).click()

    def click_create_order_button(self):
        self.driver.find_element(*OrderPageLocators.create_order_button).click()

    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    def success_string_is_displayed(self) -> bool:
        return self.driver.find_element(*OrderPageLocators.success_string).is_displayed()
