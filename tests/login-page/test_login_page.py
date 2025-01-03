import pytest
from src.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from time import sleep


class TestLoginPage:
    @pytest.fixture(scope="function")
    def page(self, browser):
        page = LoginPage(browser)
        page.go_to_page()
        return page

    def test_validate_elements_login_page(self, page):
        page.press_the_button(how=By.CSS_SELECTOR, what="[data-testid='signin-continue-btn']")
        sleep(1)