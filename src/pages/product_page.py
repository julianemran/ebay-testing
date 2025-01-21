import conftest
from .base_page import BasePage
from tests.product_page.product_page_locators import ProductPageLocators, CheckoutPageLocators


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    def go_to_page(self):
        self.open("https://www.ebay.com/")

    def search_product(self, product_name):
        self.go_to_page()
        self.fill(*ProductPageLocators.SEARCH_INPUT, filler=product_name)
        self.press_the_button(*ProductPageLocators.SEARCH_BTN)

    def validate_checkout_page(self):
        self.scroll_down(1)
        locators = {atr: getattr(CheckoutPageLocators, atr) for atr in dir(CheckoutPageLocators) if not atr.startswith("__")}
        for locator_name, locator in locators.items():
            assert self.is_element_present(*locator), f'{locator[1]} is not found in Checkout page'
            if "_INPUT" in locator_name:
                self.fill(*locator, filler=conftest.generate_random_text(4))
