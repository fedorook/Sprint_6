Sprint 6 — UI Testing Project
🧪 Project Description
This is an educational UI testing project for the scooter rental service website:
https://qa-scooter.praktikum-services.ru

The project uses Python, Selenium, pytest, and Allure for test reporting.
It follows the Page Object Model (POM) pattern.

Covered test areas:
✅ Order creation with parameterized data
✅ FAQ expansion and visibility of answers
✅ Navigation via logo clicks (Scooter logo and Yandex logo)

📁 Project Structure
Sprint_6/
├── src/
│   ├── config.py                # Base and redirect URLs
│   └── pages/
│       ├── main_page.py        # Page Object for the main page
│       └── order_page.py       # Page Object for the order form
│
├── test/
│   ├── conftest.py             # Pytest fixture for Firefox WebDriver
│   ├── test_faq.py             # Accordion FAQ tests
│   ├── test_navigation.py      # Navigation tests (logo clicks)
│   └── test_order.py           # Positive order creation scenarios
│
├── requirements.txt
└── README.md

⚙️ Installation
Install dependencies:
pip install -r requirements.txt
⚠️ Make sure geckodriver is installed and available in PATH (used for Firefox WebDriver).

▶️ Running Tests
Standard run:
pytest -v

With Allure report generation:
pytest --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure serve allure-results

📌 Test Coverage
test_order.py
Tests successful order creation with two parameterized datasets:
Top "Order" button
Bottom "Order" button

Each dataset includes:
first name, last name, address, metro station, phone number, rent date

test_faq.py
Tests the FAQ accordion section:
Expands each question by index
Asserts that the expected answer text is visible

test_navigation.py
Tests logo click behavior:
Clicking the Scooter logo brings you back to the homepage
Clicking the Yandex logo opens Dzen in a new browser tab

🔧 Tech Stack
Python 3.12 / 3.13
Selenium WebDriver
Pytest
Allure Pytest plugin
Page Object Model

🧠 Notes
All tests run in Firefox by default (can be extended to Chrome)
URLs are centralized in config.py
Page classes contain all selectors and user actions
conftest.py provides the driver fixture

👤 Author
Sergei Fedoruk