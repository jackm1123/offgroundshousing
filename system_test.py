import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

class TestSystemTests(unittest.TestCase):

    def setup(self):
        print("ye")

    def test_selenium(self):

        browser = webdriver.Chrome()

        browser.get('http://www.yahoo.com')
        assert 'Yahoo' in browser.title

        elem = browser.find_element_by_name('p')  # Find the search box
        elem.send_keys('seleniumhq' + Keys.RETURN)

        browser.quit()

    def test_selenium_ours(self):

        browser = webdriver.Chrome()

        browser.get('http://127.0.0.1:8000/listings')
        input()
        browser.quit()


if(__name__ == "__main__"):
    os.system("python3 manage.py runserver &")
    unittest.main()
    os.system("kill $(jobs -p)")
