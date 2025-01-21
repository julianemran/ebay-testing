from selenium.webdriver.common.by import By


class ProductPageLocators:
    SEARCH_INPUT = (By.ID, "gh-ac")
    SEARCH_BTN = (By.ID, "gh-search-btn")
    RESULT_LIST = (By.XPATH, "//ul[@class='srp-results srp-list clearfix']")
    NO_PRODUCT_MATCH = (By.XPATH,"//h3[normalize-space()='No exact matches found']")
    BUY_IT_NOW_BTN = (By.CSS_SELECTOR, "[data-testid='ux-call-to-action']")
    CHECKOUT_AS_GUEST_BTN = (By.XPATH, "//*[contains(text(), 'Check out as guest')]")


class CheckoutPageLocators:
    COUNTRY_SELECT = (By.ID, "country")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    ADDRESS_1_INPUT = (By.ID, "addressLine1")
    ADDRESS_2_INPUT = (By.ID, "addressLine2")
    CITY_INPUT = (By.ID, "city")
    STATE_SELECT = (By.ID, "stateOrProvince")
    POSTAL_CODE_INPUT = (By.ID, "postalCode")
    EMAIL_INPUT = (By.ID, "email")
    EMAIL_CONFIRM_INPUT = (By.ID, "emailConfirm")
    PHONE_NUMBER_INPUT = (By.ID, "phoneNumber")
    PHONE_CODE_SELECT= (By.ID, "phoneCountryCode")
    DONE_BTN = (By.CSS_SELECTOR, "[data-test-id='ADD_ADDRESS_SUBMIT']")

