"""
Test Case-5: Sorting the names by A-Z and by Z-A
Here, we have:

captured all values from the dropdown in list
then create a temp list and sort them > you will have 2 list to compare
then compare using equals method

"""
from selenium import webdriver
import time
import unittest
from pages.sorting import Sorting


class Sorting_the_names(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setting up how we want Chrome to run
        cls.browser = webdriver.Chrome(executable_path="C:/Users/Rajesh/OneDrive/Desktop/chromedriver_win32 (1)/chromedriver.exe")
        cls.browser.maximize_window()

    def test_searchPerson(self):
        browser = self.browser
        browser.get('https://octopusinvestments.com/investor/about-us/our-people/')
        sorting = Sorting(browser)
        sorting.sort_the_names()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        # To do the cleanup after test has executed.
        cls.browser.close()
        cls.browser.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main()