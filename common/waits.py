from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from custom_webdriver import expected_conditions as EC


DEFAULT_TIMEOUT = 30


class DriverWaits(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_till_url_is_updated(self, current_url, wait_time=DEFAULT_TIMEOUT, message=None):
        default_error_message = 'URL is not updated in {} seconds. current URL: \'{}\''.format(str(wait_time),
                                                                                               current_url)
        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.url_is_updated(current_url), message=error_message)

    def wait_till_element_is_present(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        default_error_message = 'Element ({}) is not attached in DOM in {} seconds. css selector: \'{}\''.format(
            css_selector, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_element_is_visible(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        default_error_message = 'Element ({}) does not get visible in {} seconds. css selector: \'{}\''.format(
            css_selector, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)), message=error_message)

    def wait_till_element_is_clickable(self, css_selector, wait_time=DEFAULT_TIMEOUT, message=None):
        default_error_message = 'Element ({}) does not get clickable in {} seconds. css selector: \'{}\''.format(
            css_selector, str(wait_time), css_selector)

        error_message = message or default_error_message

        WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)), message=error_message)
