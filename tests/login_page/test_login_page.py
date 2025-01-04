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
        page.is_element_present(*locator, timeout=5)