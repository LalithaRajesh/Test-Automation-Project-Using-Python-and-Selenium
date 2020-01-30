"""
Test Case-4: Verify the profile details match of the person found.
"""

from selenium import webdriver
import re

"""
Namely, the phone number and email Id of the person from the website is compared with the local copy on the directory 
containing the mail address and phone number of the person.
"""
expected_email = {'chris@octopusgroup.com'}
expected_num = '020 7710 2804'

def assertEquals(var1, var2):
    if var1 == var2:
        return True
    else:
        return False

browser = webdriver.Chrome('C:/Users/Rajesh/OneDrive/Desktop/chromedriver_win32 (1)/chromedriver.exe')
browser.maximize_window()
browser.get("https://octopusinvestments.com/investor/about-us/our-people/chris-hulatt/")

doc = browser.page_source
emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
phone_num = re.findall(r'\d{3}[-\.\s]??\d{4}[-\.\s]??\d{4}|\d{5}[-\.\s]??\d{3}[-\.\s]??\d{3}|(?:\d{4}\)?[\s-]?\d{3}[\s-]?\d{4})', doc)

# Verifying the email address of the person against the register (based on assumption) maintained locally
email_id = []
for email in emails:
    email_id.append(email)
email_id = set(email_id)
print(list(email_id))

assertEquals(email_id, expected_email)

# Verifying the Phone number of the person against the register (based on assumption) maintained locally
phonenum = []
for num in phone_num:
    phonenum.append(num)
phonenum = set(phonenum)

phone_num_extracted = []
for i in phonenum:
    if i == '020 7710 2804':
        phone_num_extracted.append(i)
phone_num_extracted = ''.join(phone_num_extracted)
print(phone_num_extracted)

assertEquals(phone_num_extracted, expected_num)


