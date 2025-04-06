import pytest
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage

@pytest.mark.parametrize("index, first_name, last_name, address, metro, phone, rent_date", [
    (0, "Сергей", "Иванов", "Соколово-Мещерская 6", "Планерная", "89164887784", "01.06.2025"),
    (1, "Алексей", "Петров", "Тверская 15", "Киевская", "89160001234", "15.07.2025")
])
def test_create_order(driver, index, first_name, last_name, address, metro, phone, rent_date):
    main_page = MainPage(driver)
    main_page.close_cookies()  # Close the cookies window

    # Entry point: "Order" button from top or bottom
    if index == 0:
        main_page.click_order_header()  # Entry via top button
    else:
        main_page.click_order_bottom()  # Entry via bottom button

    order_page = OrderPage(driver)
    order_page.fill_customer_info(first_name, last_name, address, metro, phone)  # Fill customer data
    order_page.click_next_button()
    order_page.fill_rent_info(rent_date)  # Fill rental information
    order_page.click_create_order_button()
    order_page.click_yes_button()  # Confirm the order

    # Check if the success message is displayed
    assert order_page.success_string_is_displayed()
