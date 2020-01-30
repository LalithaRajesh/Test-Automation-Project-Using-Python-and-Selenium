"""
Test Case-6: Verify if the sorting order is correct or not
"""
from selenium import webdriver
browser = webdriver.Chrome('C:/Users/Rajesh/OneDrive/Desktop/chromedriver_win32 (1)/chromedriver.exe')
browser.maximize_window()
browser.get('https://octopusinvestments.com/investor/about-us/our-people/')
findname = browser.find_elements_by_class_name("team-item_title")

"""
Verifying whether the Sort is by A-Z(Ascending) order:
"""
i = 0
sizeofList = len(findname)
ascendingorderchkflag = True
while i < sizeofList-1 :
#     print(findname[i].get_attribute("textContent"))
    f1=findname[i].get_attribute("textContent")
    f2=findname[i+1].get_attribute("textContent")
#     print (f2)
    if f1>f2:
        ascendingorderchkflag = False
    i+=1
if ascendingorderchkflag == True:
    print("A to Z Ascending Order looks good - PASS")
else:
    print("A to Z Ascending Order FAILED")

"""
 Verifying whether the Sort is by Z-A(Descending) order:
"""
descendingorderchkflag = True
while i < sizeofList-1 :
    f1=findname[i+1].get_attribute("textContent")
    f2=findname[i].get_attribute("textContent")
    if f1<f2:
        descendingorderchkflag = False
    i+=1
if descendingorderchkflag == True:
    print("Z to A Descending Order looks good - PASS")
else:
    print("Z to A Descending Order FAILED")