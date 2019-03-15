import unittest

import crawler

class TestCrawler(unittest.TestCase):

    def test_check_if_url_is_absolute(self):
        self.assertTrue(crawler.is_absolute("http://www.google.pl"))

    def test_check_if_url_is_relative(self):
        self.assertFalse(crawler.is_absolute("/"))

    def test_show_error_message_while_parsing_incorrect_url(self):
        self.assertIn("Invalid url", str(crawler.parse_html_page("incorrect url")))

    def test_show_error_message_while_parsing_not_existing_host(self):
        self.assertIn("Failed to establish a new connection with url", str(crawler.parse_html_page("http://www.devilpa")))

if __name__ == '__main__':
    unittest.main()
