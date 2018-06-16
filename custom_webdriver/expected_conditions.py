from selenium.webdriver.support.expected_conditions import *


class url_is_updated(object):
    def __init__(self, current_url):
        self.current_url = current_url

    def __call__(self, driver):
        return driver.current_url != self.current_url


def _find_element(driver, by):
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e


def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e