from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-testid='signin-continue-btn']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid='userid']")
    GOOGLE_SIGNIN_BTN = (By.ID, "signin_ggl_btn")
    FACEBOOK_SIGNIN_BTN = (By.ID, "signin_fb_btn")
    APPLE_SIGNIN_BTN = (By.ID, "signin_appl_btn")
    CREATE_ACCOUNT_BTN = (By.ID, "create-account-link")
    STAY_LOGIN_CHECKBOX = (By.XPATH, "//input[@id='kmsi-checkbox']")
    OPEN_SIGNIN_BTN = (By.XPATH, "//a[normalize-space()='Sign in']")
    ERROR_MSG = (By.ID, "signin-error-msg")
    PASS_INPUT = (By.XPATH, "//input[@id='pass']")
    SIGNIN_BTN_PASS_PAGE = (By.ID, "sgnBt")
    PASSKEY_TITLE = (By.ID, "passkeys-title")