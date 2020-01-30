"""
Test Case -3: Click on the Image of the person
"""

from selenium import webdriver
import time
import unittest
from pages.aboutus import aboutUs

"""
The page searches for 'Chris Hulatt' and clicks his image.
"""
class Click_image(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setting up how we want Chrome to run
        cls.browser = webdriver.Chrome(executable_path="C:/Users/Rajesh/OneDrive/Desktop/chromedriver_win32 (1)/chromedriver.exe")
        cls.browser.maximize_window()

    def test_click_image(self):
        browser = self.browser
        browser.get('https://octopusinvestments.com/investor/about-us/our-people/')
        aboutus = aboutUs(browser)
        aboutus.enter_searchUserName("Chris Hulatt")
        time.sleep(5)
        click_image = browser.get("https://octopusinvestments.com/investor/about-us/our-people/chris-hulatt/")
        print (click_image)
        time.sleep(7)

    @classmethod
    def tearDownClass(cls):
        # To do the cleanup after test has executed.
        cls.browser.close()
        cls.browser.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()