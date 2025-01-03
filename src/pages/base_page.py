import sys
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def control_btn():
    if sys.platform == "darwin":
        return Keys.COMMAND
    else:
        return Keys.CONTROL


class BasePage:
    def __init__(self, browser, *args, **kwargs):
        super(BasePage, self).__init__(*args, **kwargs)
        self.browser = browser
        self.url = "https://www.ebay.com/"

    def open(self, link):
        current_url = self.browser.current_url.replace('www.', '')
        if current_url != link:
            self.browser.get(link)

    def find_element(self, how, what, timeout=10):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except Exception as e:
            raise Exception(f"{e}\nProblem with finding {what}")
        return element

    def is_element_present(self, how, what, timeout=20, element=None):
        if element is None:
            element = self.browser
        try:
            WebDriverWait(element, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def press_the_button(self, how, what, element_appeared=None, timeout=10, is_to_scroll=True):
        """how: which type of selectors is used, ex., By.CSS_SELECTOR
           what: elements selector itself that should be filled, ex., [id='username']
           element_appeared: page element that appears after the pressing the button; consists of 2 params: how, what
        """
        try:
            button = self.find_element(how, what, timeout=timeout)
            WebDriverWait(self.browser, timeout=timeout).until_not(EC.staleness_of(button))
            actions = ActionChains(self.browser)
        except TimeoutException:
            raise TimeoutException(f"element {what} didn't appear in {timeout} secs")
        if is_to_scroll:
            actions.move_to_element(button).perform()
        try:
            button.click()
        except Exception as e:
            raise Exception(f"{e}\nFailed to click on {what}")
        if element_appeared is not None:
            assert self.is_element_present(*element_appeared, timeout=timeout), f'{element_appeared} did not appear'

    def fill(self, how, what, filler, clean=False, write_speed=None):
        """how: type of selector
           what: what element to fill
           filler: what to type into the element's field
           write_speed: the time to wait between each char"""
        element = self.find_element(how, what)
        if clean:
            try:
                element.send_keys(control_btn() + "a")
                element.send_keys(Keys.DELETE)
            except Exception as e:
                raise Exception(f"{e}\nProblem with typing in {what}")
        if filler is not None:
            try:
                if write_speed:
                    for fill in filler:
                        element.send_keys(fill)
                        sleep(write_speed)
                else:
                    element.send_keys(filler)
            except Exception as e:
                raise Exception(f"{e}\nProblem with typing in {what}")
        return element.get_attribute('value')

