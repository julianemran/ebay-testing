import os
import allure
import pytest
from tests.frontend_report import FrontendReport
from src.pages.login_page import LoginPage
from tests.login_page.login_page_locators import LoginPageLocators


class TestLoginPage(FrontendReport):
    @pytest.fixture(scope="function")
    def page(self, browser):
        page = LoginPage(browser)
        page.go_to_page()
        return page

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('locator', [getattr(LoginPageLocators, attr) for attr in dir(LoginPageLocators) if not attr.startswith("__")])
    def test_validate_elements_login_page(self, page, locator):
        allure.dynamic.description("This test validates the presence of elements on the login page.")
        assert page.is_element_present(*locator, timeout=5), f'{locator[1]} is not found'

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('user_email', ["not-email", "fake@emailcom"])
    def test_login_invalid_email(self, page, user_email):
        allure.dynamic.description(f"This test attempts to log in with invalid email=[{user_email}], and checks for error messages.")
        page.fill(*LoginPageLocators.USERNAME_INPUT, filler=user_email, clean=True)
        page.press_the_button(*LoginPageLocators.SIGNIN_BTN)
        assert page.is_element_present(*LoginPageLocators.ERROR_MSG), f'Error text not found'

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_full_flow(self, page):
        allure.dynamic.description("This test attempts to log into the website using a login and a password. Fails if any error happens.")
        page.fill(*LoginPageLocators.USERNAME_INPUT, filler=os.getenv("EBAY_EMAIL"), clean=True)
        page.press_the_button(*LoginPageLocators.SIGNIN_BTN)
        page.fill(*LoginPageLocators.PASS_INPUT, filler=os.getenv("EBAY_PASS"), clean=True)
        page.press_the_button(*LoginPageLocators.SIGNIN_BTN_PASS_PAGE)
        assert page.is_element_present(*LoginPageLocators.PASSKEY_TITLE), (f'The Website should redirect the user '
                                                                           f'to passkey title page')
