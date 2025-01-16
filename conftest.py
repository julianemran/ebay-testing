import sys
import pytest
from pyvirtualdisplay import Display
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


def get_chrome_browser_options():
    """Configure Chrome options for legitimate automated testing."""
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
    # Start a virtual display
    if sys.platform == "linux":
        display = Display(visible=0, size=(1920, 1080))
        display.start()

    # Initialize the browser with the specified options
    new_browser = uc.Chrome(use_subprocess=True, options=get_chrome_browser_options())
    new_browser.implicitly_wait(3)
    yield new_browser
    # Ensure the browser and display are cleaned up
    new_browser.quit()
    if sys.platform == "linux":
        display.stop()
