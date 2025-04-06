# src/pages/main_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    cookies_btn = (By.ID, "rcc-confirm-button")
    order_btn_header = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    order_btn_bottom = (By.XPATH, "//div[contains(@class, 'FinishButton')]/button[text()='Заказать']")
    question_id = "accordion__heading-{}"
    answer_xpath = "//div[contains(@id, 'accordion__panel')][.='{}']"
    logo_scooter = (By.XPATH, '//img[@alt="Scooter"]')
    logo_yandex = (By.XPATH, '//img[@alt="Yandex"]')


    def click_order_header(self):
        self.driver.find_element(*self.order_btn_header).click()

    def click_order_bottom(self):
        self.driver.find_element(*self.order_btn_bottom).click()

    def close_cookies(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.cookies_btn))
        self.driver.find_element(*self.cookies_btn).click()

    def expand_question(self, index: int):
        question = self.driver.find_element(By.ID, self.question_id.format(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(question))
        question.click()

    def is_answer_visible(self, text: str) -> bool:
        locator = (By.XPATH, self.answer_xpath.format(text))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()

    def click_logo_scooter(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logo_scooter))
        self.driver.find_element(*self.logo_scooter).click()

    def click_logo_yandex(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logo_yandex))
        self.driver.find_element(*self.logo_yandex).click()