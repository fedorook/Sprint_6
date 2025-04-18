# src/pages/main_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage
from src.pages.locators import MainPageLocators

class MainPage(BasePage):
    def click_order_header(self):
        self.click(MainPageLocators.order_btn_header)

    def click_order_bottom(self):
        self.click(MainPageLocators.order_btn_bottom)

    def close_cookies(self):
        self.click(MainPageLocators.cookies_btn)

    def expand_question(self, index: int):
        question_locator = (By.ID, MainPageLocators.question_id.format(index))
        question = self.find(question_locator)
        self.scroll_to(question)
        self.wait.until(EC.element_to_be_clickable(question_locator))
        question.click()

    def is_answer_visible(self, text: str) -> bool:
        locator = (By.XPATH, MainPageLocators.answer_xpath.format(text))
        self.wait_for_visibility(locator)
        return self.find(locator).is_displayed()

    def click_logo_scooter(self):
        self.click(MainPageLocators.logo_scooter)

    def click_logo_yandex(self):
        self.click(MainPageLocators.logo_yandex)
