import time
import pytest
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def get_chrome_browser_options():
    """Configure Chrome options for legitimate automated testing"""
    options = Options()

    # Basic required options
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    return options

@pytest.fixture(scope="class")
def browser():
    new_browser = uc.Chrome(use_subprocess=True, options=get_chrome_browser_options())
    new_browser.implicitly_wait(3)
    yield new_browser
    new_browser.quit()

