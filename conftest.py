import re
import os
import sys
import pytest
import subprocess
from pyvirtualdisplay import Display
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchWindowException


def get_chrome_version():
    try:
        result = subprocess.run(['google-chrome', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            version_output = result.stdout.strip()
            match = re.search(r'(\d+)\.', version_output)
            if match:
                return int(match.group(1))  # Return as an integer
        return  None
    except:
        return None


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
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL', 'browser': 'ALL'})
    return options


@pytest.fixture(scope="class")
def browser():
    version_main = None
    # Start a virtual display
    if sys.platform == "linux":
        version_main = get_chrome_version()
        display = Display(visible=0, size=(1920, 1080))
        display.start()

    # Initialize the browser with the specified options
    new_browser = uc.Chrome(use_subprocess=True, options=get_chrome_browser_options(), version_main=version_main)
    new_browser.implicitly_wait(3)
    yield new_browser
    # Ensure the browser and display are cleaned up
    new_browser.quit()
    if sys.platform == "linux":
        display.stop()


def is_browser_open(browser):
    try:
        browser.title
    except NoSuchWindowException:
        return False
    return True

def get_console_logs(browser, request):
    logs = browser.get_log("browser")
    logs_text = ""
    for entry in logs:
        if "message" in entry:
            logs_text += f"{entry['message']} \n ------------\n"

    if logs_text:
        file_path = f"{request.node.name.replace('/', '_')}"
        file_path = file_path[:50]  # to take only first 50 character for long test names
        if not os.path.exists("reports"):
            if sys.platform == "win32":
                subprocess.run(["mkdir", "reports"], shell=True)
            else:
                subprocess.run(["mkdir", "reports"])
        file_path = f"./reports/{file_path}_console.txt"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(logs_text)
        return file_path
    return None