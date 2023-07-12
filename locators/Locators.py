
from selenium.webdriver.common.by import By
from selenium import webdriver

print('-Identify by ID-')

chrome = webdriver.Chrome()
chrome.get('https://www.webdriveruniversity.com/Login-Portal/index.html')
chrome.implicitly_wait(5)
chrome.quit()

chrome.find_element(By.ID,"text").send_keys("Andreea")
chrome.find_element(By.ID, "password").send_keys("password")
chrome.find_element(By.ID, "login-button").click()

print('-Identify by Name-')

chrome = webdriver.Chrome()
chrome.get('https://www.webdriveruniversity.com/Contact-Us/contactus.html')

chrome.find_element(By.NAME, "first_name").send_keys("Andreea")
chrome.find_element(By.NAME, "last_name").send_keys("Popa")
chrome.find_element(By.NAME, "email").send_keys("andreeapopa9793@gmail.com")

print('-Identify by Link Text-')

chrome = webdriver.Chrome()
chrome.get('https://www.webdriveruniversity.com/Page-Object-Model/index.html')
chrome.find_element(By.LINK_TEXT, "Home").click()
chrome.find_element(By.LINK_TEXT, "Our Products").click()
chrome.find_element(By.LINK_TEXT, "Contact Us").click()

print('-Identify by Class Name-')

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.CLASS_NAME, "btn btn-lg btn-primary").click()

print('-Identify by CSS Selector-')

chrome.find_element(By.CSS_SELECTOR, '#first-name') #css locator by ID
chrome.find_element(By.CSS_SELECTOR, '.form-control')[1].send_keys('keys') #css locator by Class
chrome.find_element(By.CSS_SELECTOR, "input[placeholder=''Enter your job title']").send_keys('qa') #css locator by tag and attribute
chrome.find_element(By.CSS_SELECTOR, "div[class='col-sm-8 col-sm-offset-2'] > strong > label[for='radio-button']")[1].text #css by siblings
chrome.find_element(By.CSS_SELECTOR, "div[class='col-sm-4'] > input").text

chrome = webdriver.Chrome()
chrome.get('https://www.webdriveruniversity.com/To-Do-List/index.html')

#identify list element
chrome.find_element(By.CSS_SELECTOR, "ul li:nth-child(1)")
chrome.find_element(By.CSS_SELECTOR, "ul li:nth-last-child(1)")
chrome.find_element(By.CSS_SELECTOR, "ul li:nth-of-type(3)")
chrome.find_element(By.CSS_SELECTOR, "ul li:nth-last-of-type(2)")

print('-Identify by XPATH-')

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Andreea") # * replaced the tag
chrome.find_element(By.XPATH, '//input[@placeholder="Enter last name"]').send_keys("Popa") # by tag and attribute
chrome.find_element(By.XPATH, '//div/div/input[@id="job-title"]').send_keys("qa") #via relative Xpath to the child of the specified tag
chrome.find_element(By.XPATH, '//form//input[@value="radio-button-2"]').click() # by relative Xpath to a relative child
chrome.find_element(By.XPATH, '//input[@id="checkbox-2"]/parent::div/preceding-sibling::div/input').click() # via relative Xpath to a sibling
chrome.find_element(By.XPATH, "//form/div/div/following-sibling::div[4]/preceding-sibling::div[3]")
chrome.find_element(By.XPATH, "//form/div/div/following-sibling::div[1]").send_keys("qa")
chrome.find_element(By.XPATH, "//form/div/div/preceding-sibling::div").send_keys("Andreea")
chrome.find_element(By.XPATH, "//a[.='Submit']").click() #this can also be
chrome.find_element(By.XPATH, "//a[contains(text(),'Submit')]") #for partial text of the link
chrome.find_element(By.XPATH, "//a[contains(.,'Submit')]").click() #replaced 'text()' with 'dot'


chrome = webdriver.Chrome()
chrome.get('https://www.webdriveruniversity.com/To-Do-List/index.html')

chrome.find_element(By.XPATH, "//div[@id='container']/ul/li[1]") #Identify list element


























