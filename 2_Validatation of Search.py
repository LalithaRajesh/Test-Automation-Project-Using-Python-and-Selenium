"""
Test Case -2: Validate if the correct person was found
"""

from selenium import webdriver
import urllib.request
import cv2

"""                 
In order to validate if the correct person was found, we are going to compare it with the images obtained from the web and the image which we already had in
the local repository. Such that, it provides the differences if there is any.
"""

browser = webdriver.Chrome('C:/Users/Rajesh/OneDrive/Desktop/chromedriver_win32 (1)/chromedriver.exe')
browser.maximize_window()
browser.get('https://octopusinvestments.com/investor/about-us/our-people/')
search = browser.find_element_by_name('search')
search.send_keys("Chris Hulatt")
ids = browser.find_elements_by_xpath("//input[@placeholder='e.g Ruth Handcock']")
time.sleep(5)
for i in ids:
    print ("The result for 'Chris Hulatt' is seen on the screen", i.text)

# get the image source
image = browser.find_element_by_xpath("//img[@class='attachment-team-thumb size-team-thumb wp-post-image']").get_attribute('src')
print(image)

"""
#The below code pulls the image source from the website and saves it to the local repository
"""

url = 'https://octopusinvestments.com/investor/wp-content/uploads/Chris-Hulatt-1.jpg'
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'whatever')
filename, headers = opener.retrieve(url, 'C:/Users/Rajesh/OneDrive/Desktop/chris.jpg')

"""
This code uses OpenCV to compare between two images and finds the difference between them.
"""

original = cv2.imread("C:/Users/Rajesh/OneDrive/Desktop/Source-Chris-Hulatt-1.jpg")
duplicate = cv2.imread("C:/Users/Rajesh/OneDrive/Desktop/Target-Chris-Hulatt.jpg")
if original.shape == duplicate.shape:
    print("The images have same size and channels")
else:
    print("There are difference with size and channels")
difference = cv2.subtract(original, duplicate)
b, g, r = cv2.split(difference)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("The images are completely Equal")
else:
    print ("The images are not equal")
cv2.imshow("Original", original)
cv2.imshow("Duplicate", duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()