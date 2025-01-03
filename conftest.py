import pytest
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


def get_chrome_browser_options():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL', 'browser': 'ALL'})
    # options.add_argument("--headless")
    return options


@pytest.fixture(scope="module")
def browser():
    new_browser = uc.Chrome(use_subprocess=True, options=get_chrome_browser_options())
    yield new_browser
    new_browser.quit()

