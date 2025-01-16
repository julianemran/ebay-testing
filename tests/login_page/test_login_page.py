import os
import pytest
from src.pages.login_page import LoginPage
from tests.login_page.login_page_locators import LoginPageLocators


class TestLoginPage:
    @pytest.fixture(scope="function")
    def page(self, browser):
        page = LoginPage(browser)
        page.go_to_page()
        return page

    @pytest.mark.parametrize('locator', [getattr(LoginPageLocators, attr) for attr in dir(LoginPageLocators) if not attr.startswith("__")])
    def test_validate_elements_login_page(self, page, locator):
        assert page.is_element_present(*locator, timeout=5), f'{locator[1]} is not found'

    @pytest.mark.parametrize('user_email', ["not-email", "fake@emailcom"])
    def test_login_invalid_email(self, page, user_email):
        page.fill(*LoginPageLocators.USERNAME_INPUT, filler=user_email, clean=True)
        page.press_the_button(*LoginPageLocators.SIGNIN_BTN)
        assert page.is_element_present(*LoginPageLocators.ERROR_MSG), f'Error text not found'

    def test_login_full_flow(self, page):
        #viveyak930@fanicle.com
        page.fill(*LoginPageLocators.USERNAME_INPUT, filler=os.getenv("EBAY_EMAIL"), clean=True)
        page.press_the_button(*LoginPageLocators.SIGNIN_BTN)
        page.fill(*LoginPageLocators.PASS_INPUT, filler=os.getenv("EBAY_PASS"), clean=True)
        page.press_the_button(*LoginPageLocators.SIGNIN_BTN_PASS_PAGE)
        assert page.is_element_present(*LoginPageLocators.PASSKEY_TITLE), (f'The Website should redirect the user '
                                                                           f'to passkey title page')
