import time
class Sorting():

    def __init__(self, browser):
        self.browser = browser
        self.search = "search"

    def sort_the_names(self):
        self.browser.find_element_by_name(self.search).clear()
        self.browser.find_element_by_xpath("//div[@class='jq-selectbox__select-text']").click()
        self.browser.find_element_by_xpath("//li[contains(text(),'Sort A-Z')]").click()
        self.browser.find_element_by_xpath("//div[@class='jq-selectbox__select-text']").click()
        self. browser.find_element_by_xpath("//li[contains(text(),'Sort Z-A')]").click()