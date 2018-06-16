import time

from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from tests.base import TrivagoTestCase
from common.utils import append_test_log


fake = Faker()


class SearchTrivagoTest(TrivagoTestCase):
    css_selector_for_search_input = '.search-input-wrapper input'
    css_selector_for_no_result = '.no-results'
    css_selector_for_search_result_title = '.search-results h3.section-title'
    css_selector_for_search_icon = '.search-icon'
    
    def _search_by_keyword(self, keyword):
        append_test_log(self.test_case_name, '#'*20 + '\n' + 'Search for: {}\n'.format(keyword))

        search_input = self.driver.find_element_by_css_selector(self.css_selector_for_search_input)

        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)
        append_test_log(self.test_case_name, 'Waiting for search results\n')
        time.sleep(2)

        try:
            self.driver_waits.wait_till_element_is_visible(self.css_selector_for_search_result_title, wait_time=10)
        except TimeoutException:
            no_result_element = self.driver.find_element_by_css_selector(self.css_selector_for_no_result)
            assert no_result_element.is_displayed(), 'Something wrong in search result page'
            append_test_log(self.test_case_name, 'No result found\n')
        else:
            search_result_title_element = self.driver.find_element_by_css_selector(
                self.css_selector_for_search_result_title)
            append_test_log(self.test_case_name, 'Output: {}\n'.format(search_result_title_element.text))


    def test_search_by_destination(self):
        self.test_case_name = 'search-by-destination'
        append_test_log(self.test_case_name, 'Test Case log for: Search by destination\n', mode='w+')

        self.driver_waits.wait_till_element_is_clickable(self.css_selector_for_search_icon)

        append_test_log(self.test_case_name, 'Search icon appeared\n')

        self.driver.find_element_by_css_selector(self.css_selector_for_search_icon).click()

        self.driver_waits.wait_till_element_is_visible(self.css_selector_for_search_input)
        append_test_log(self.test_case_name, 'Search box appeared\n')

        css_selector_for_destination_filter = '.search-tags .swiper-wrapper'
        self.driver_waits.wait_till_element_is_visible(css_selector_for_destination_filter)
        append_test_log(self.test_case_name, 'Destination filter appeared\n')

        destinations = ['Canada', 'Europe', 'International', fake.country()]

        for d in destinations:
            self._search_by_keyword(d)






