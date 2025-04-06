from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    subway_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    station_menu_item = "//div[text()='%s']"
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_period_input = (By.XPATH, "//div[text()='* Срок аренды']")
    rent_period_menu_item = (By.XPATH, "//div[text()='трое суток']")
    create_order_button = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")
    yes_button = (By.XPATH, "//button[text()='Да']")
    success_string = (By.XPATH, "//div[text()='Заказ оформлен']")

    def fill_customer_info(self, first_name: str, last_name: str, address: str, metro: str, phone: str):
        self.driver.find_element(*self.name_input).send_keys(first_name)
        self.driver.find_element(*self.lastname_input).send_keys(last_name)
        self.driver.find_element(*self.address_input).send_keys(address)

        self.driver.find_element(*self.subway_input).click()
        station_locator = (By.XPATH, self.station_menu_item % metro)
        station_menu = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(station_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", station_menu)
        station_menu.click()

        self.driver.find_element(*self.phone_input).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def fill_rent_info(self, rent_date: str):
        self.driver.find_element(*self.date_input).send_keys(rent_date, Keys.ENTER)
        self.driver.find_element(*self.rent_period_input).click()
        self.driver.find_element(*self.rent_period_menu_item).click()

    def click_create_order_button(self):
        self.driver.find_element(*self.create_order_button).click()

    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    def success_string_is_displayed(self) -> bool:
        return self.driver.find_element(*self.success_string).is_displayed()
