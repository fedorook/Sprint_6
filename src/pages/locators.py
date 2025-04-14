from selenium.webdriver.common.by import By

class MainPageLocators:
    cookies_btn = (By.ID, "rcc-confirm-button")
    order_btn_header = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    order_btn_bottom = (By.XPATH, "//div[contains(@class, 'FinishButton')]/button[text()='Заказать']")
    question_id = "accordion__heading-{}"
    answer_xpath = "//div[contains(@id, 'accordion__panel')][.='{}']"
    logo_scooter = (By.XPATH, '//img[@alt="Scooter"]')
    logo_yandex = (By.XPATH, '//img[@alt="Yandex"]')

class OrderPageLocators:
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