from .base_page import BasePage
from tests.signup_page.signup_page_locators import SignupPageLocators


class SignupPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SignupPage, self).__init__(*args, **kwargs)

    def go_to_page(self):
        self.open("https://signup.ebay.com/pa/crte?ru=")

    def fill_signup_page(self, attributes):
        for key, val in attributes.items():
            locator = getattr(SignupPageLocators, f"{key.upper()}_INPUT")
            self.fill(*locator, val, clean=True)
