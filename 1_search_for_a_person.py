"""
Test Case-1: Search for a Person
"""

from selenium import webdriver
import time
import unittest
from pages.aboutus import aboutUs


class Test_AboutUs_Search_Base(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setting up how we want Chrome to run
        cls.browser = webdriver.Chrome(executable_path="C:/Users/Rajesh/OneDrive/Desktop/chromedriver_win32 (1)/chromedriver.exe")
        cls.browser.maximize_window()

    def test_searchPerson(self):
        browser = self.browser
        browser.get('https://octopusinvestments.com/investor/about-us/our-people/')
        aboutus = aboutUs(browser)
        aboutus.enter_searchUserName("Chris Hulatt")
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        # To do the cleanup after test has executed.
        cls.browser.close()
        cls.browser.quit()
        print("Test completed")


# # Test class containing methods corresponding to testcases.
# class Test_AboutUs_Search(Test_AboutUs_Search_Base):
#     def setUp(self):
#         # to call the setUp() method of base class or super class.
#         super().setUp()

if __name__ == '__main__':
    unittest.main()
