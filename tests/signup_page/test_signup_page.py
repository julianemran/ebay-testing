import allure
import pytest
import conftest
from selenium.webdriver.common.by import By
from src.pages.signup_page import SignupPage
from tests.frontend_report import FrontendReport
from tests.signup_page.signup_page_locators import SignupPageLocators


class TestSignupPage(FrontendReport):
    @pytest.fixture(scope="function")
    def page(self, browser):
        page = SignupPage(browser)
        page.go_to_page()
        return page

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('locator', [getattr(SignupPageLocators, attr) for attr in dir(SignupPageLocators) if not attr.startswith("__")])
    def test_validate_elements_login_page(self, page, locator):
        allure.dynamic.description("This test validates the presence of elements on the Signup page.")
        assert page.is_element_present(*locator, timeout=5), f'{locator[1]} is not found'

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('attrs, error_msg', [
        ({
            "first_name": conftest.generate_random_text(6),
            "last_name": conftest.generate_random_text(6),
            "email": "invalid_email",
            "password": "#EbayTesting12"
        }, "Email address is invalid"),
        ({
            "first_name": "",
            "last_name": conftest.generate_random_text(6),
            "email": f"{conftest.generate_random_text(14)}121@gmail.com",
            "password": "#EbayTesting12"
        }, "Please enter your first name"),
        ({
            "first_name": conftest.generate_random_text(6),
            "last_name": conftest.generate_random_text(6),
            "email": f"{conftest.generate_random_text(14)}121@gmail.com",
            "password": "badpass"
        }, "at least 8 characters"),
    ])
    def test_signup_invalid_data(self, page, attrs, error_msg):
        allure.dynamic.description(f"This test attempts to signup with invalid attributes, and checks for error messages.")
        page.fill_signup_page(attributes=attrs)
        page.press_the_button(*SignupPageLocators.CREATE_ACCOUNT_BTN)
        assert page.is_element_present(By.XPATH, f"//*[contains(text(), '{error_msg}')]"), \
            f"Error msg with text=[{error_msg}] not found"

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('attrs', [
        {
             "first_name": conftest.generate_random_text(6),
             "last_name": conftest.generate_random_text(6),
             "email": f"{conftest.generate_random_text(7)}124@gmail.com",
             "password": "#EbayTesting12"
        }
    ])
    def test_signup(self, page, attrs):
        allure.dynamic.description(f"This test attempts to signup with valid attributes.")
        page.fill_signup_page(attributes=attrs)
        page.press_the_button(*SignupPageLocators.CREATE_ACCOUNT_BTN)
        assert page.is_element_present(*SignupPageLocators.PHONE_NUMBER_INPUT), "Should redirect to Add phone number page"