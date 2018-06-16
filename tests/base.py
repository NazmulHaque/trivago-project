from unittest import TestCase

from selenium import webdriver

import settings
from common.waits import DriverWaits


class TrivagoTestCase(TestCase):
    browser = settings.DEFAULT_BROWSER
    base_url = settings.BASE_URL

    @classmethod
    def setUpClass(cls):
        cls.driver = getattr(webdriver, cls.browser)()
        cls.driver.maximize_window()

        cls.driver_waits = DriverWaits(cls.driver)

        cls.driver.get(cls.base_url)
        cls.driver_waits.wait_till_url_is_updated(settings.BASE_URL)
        current_url = cls.driver.current_url
        print(current_url)
        assert current_url == settings.REDIRECT_URL, "The site is not redirected to currect url. " \
                                                                "redirected to {}".format(current_url)

        css_selector_for_hero_button = '.hero-button'
        cls.driver_waits.wait_till_element_is_present(css_selector_for_hero_button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

