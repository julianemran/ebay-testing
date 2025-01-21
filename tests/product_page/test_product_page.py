import allure
import pytest
import conftest
from selenium.webdriver.common.by import By
from src.pages.product_page import ProductPage
from tests.frontend_report import FrontendReport
from tests.product_page.product_page_locators import ProductPageLocators


class TestSignupPage(FrontendReport):

    @pytest.fixture(scope="function")
    def page(self, browser):
        page = ProductPage(browser)
        page.go_to_page()
        return page

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('product_name, element_to_present',
                             [
                                 ("iphone 16 case", ProductPageLocators.RESULT_LIST),
                                 (conftest.generate_random_text(40), ProductPageLocators.NO_PRODUCT_MATCH)
                             ])
    def test_search_product(self, page, product_name, element_to_present):
        allure.dynamic.description("Test the search functionality on the product page. Asserts "
                                   "that the specified element is present on the page after performing the search")
        page.search_product(product_name=product_name)
        assert page.is_element_present(*element_to_present), f'{element_to_present[1]} is not found'


    @allure.severity(allure.severity_level.CRITICAL)
    def test_buy_product_page(self, page):
        allure.dynamic.description("Test the buy functionality on the product page. Asserts that the user can "
                                   "search for a product, navigate to its page, and proceed to checkout as a guest.")
        page.search_product(product_name="Jolochip")
        product_list = page.find_element(*ProductPageLocators.RESULT_LIST)
        first_item = product_list.find_element(By.TAG_NAME, "li")
        product_link = first_item.find_element(By.TAG_NAME, 'a').get_attribute("href")
        page.open(link=product_link)
        page.press_the_button(*ProductPageLocators.BUY_IT_NOW_BTN)
        page.press_the_button(*ProductPageLocators.CHECKOUT_AS_GUEST_BTN)
        page.validate_checkout_page()

