from unittest import TestCase

from selenium import webdriver

import settings


class TrivagoTestCase(TestCase):
    browser = settings.DEFAULT_BROWSER
    base_url = settings.BASE_URL

    @classmethod
    def setUpClass(cls):
        cls.driver = getattr(webdriver, settings.DEFAULT_BROWSER)()
        cls.driver.maximize()
        cls.driver.get(settings)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

