
class aboutUs():


    def __init__(self, browser):
        self.browser = browser

        self.aboutUs_text = "Our story"
        self.search = "search"

    def enter_searchUserName(self, userName):
        self.browser.find_element_by_name(self.search).clear()
        self.browser.find_element_by_name(self.search).send_keys(userName)
        ids = self.browser.find_elements_by_xpath("//input[@placeholder='e.g Ruth Handcock']")
        for i in ids:
            print("The search result for Chris are printed:", i.text)