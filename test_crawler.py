import unittest

import crawler
from page import Page

class TestCrawler(unittest.TestCase):

    def test_check_if_url_is_absolute(self):
        self.assertTrue(Page.is_absolute("http://www.google.pl"))

    def test_check_if_url_is_relative(self):
        self.assertFalse(Page.is_absolute("/"))

    def test_show_error_message_while_parsing_incorrect_url(self):
        self.assertIn("Invalid url", str(crawler.parse_html_page("incorrect url")))

    def test_show_error_message_while_parsing_not_existing_host(self):
        self.assertIn("Failed to establish a new connection with url", str(crawler.parse_html_page("http://www.devilpa")))

    def test_number_of_links_is_greater_than_0(self):
        self.assertGreater(len(crawler.get_list_of_links_for_domain("http://www.link.pl", "http://www.link.pl", "<a href=\"http://www.link.pl\"></a>", 0)), 0)

    def test_number_of_links_is_equal_0(self):
        self.assertEqual(len(crawler.get_list_of_links_for_domain("http://www.link.pl", "http://www.link.pl", "", 0)), 0)

if __name__ == '__main__':
    unittest.main()
