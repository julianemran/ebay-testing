from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def go_to_page(self):
        self.open("https://signin.ebay.com/ws/eBayISAPI.dll?SignIn")