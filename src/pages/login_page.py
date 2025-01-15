from .base_page import BasePage
from tests.login_page.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def go_to_page(self):
        if "eBayISAPI.dll?SignIn" in self.browser.current_url:
            return
        self.open("https://www.ebay.com/")
        self.press_the_button(*LoginPageLocators.OPEN_SIGNIN_BTN, element_appeared=LoginPageLocators.USERNAME_INPUT)