from selenium.webdriver.common.by import By


class SignupPageLocators:
    PERSONAL_RADIO_BTN = (By.ID, "personalaccount-radio")
    BUSINESS_RADIO_BTN = (By.ID, "businessaccount-radio")
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "password")
    CREATE_ACCOUNT_BTN = (By.ID, "EMAIL_REG_FORM_SUBMIT")
    SIGNUP_WITH_GOOGLE = (By.ID, "google")
    SIGNUP_WITH_FACEBOOK = (By.ID, "facebook")
    SIGNUP_WITH_APPLE = (By.ID, "apple")
    SIGNIN_BTN = (By.XPATH, "//a[normalize-space()='Sign in']")
    PHONE_NUMBER_INPUT = (By.ID, "phoneCountry")

