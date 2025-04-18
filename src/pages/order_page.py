# src/pages/order_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.base_page import BasePage
from src.pages.locators import OrderPageLocators

class OrderPage(BasePage):
    def fill_customer_info(self, first_name: str, last_name: str, address: str, metro: str, phone: str):
        self.find(OrderPageLocators.name_input).send_keys(first_name)
        self.find(OrderPageLocators.lastname_input).send_keys(last_name)
        self.find(OrderPageLocators.address_input).send_keys(address)

        self.click(OrderPageLocators.subway_input)

        station_locator = (By.XPATH, OrderPageLocators.station_menu_item % metro)
        station_menu = self.wait_for_visibility(station_locator)
        self.scroll_to(station_menu)
        station_menu.click()

        self.find(OrderPageLocators.phone_input).send_keys(phone)

    def click_next_button(self):
        self.click(OrderPageLocators.next_button)

    def fill_rent_info(self, rent_date: str):
        self.find(OrderPageLocators.date_input).send_keys(rent_date, Keys.ENTER)
        self.click(OrderPageLocators.rent_period_input)
        self.click(OrderPageLocators.rent_period_menu_item)

    def click_create_order_button(self):
        self.click(OrderPageLocators.create_order_button)

    def click_yes_button(self):
        self.click(OrderPageLocators.yes_button)

    def success_string_is_displayed(self) -> bool:
        return self.find(OrderPageLocators.success_string).is_displayed()
