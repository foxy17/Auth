from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser =webdriver.Chrome(r"C:\Users\tanmay jain\Desktop\chromedriver")


#url=input()
username="tj2023"
password="Pass@1373"
def hrLogin():
    url="https://www.hackerrank.com/auth/login"
    browser.get(url)
    email=browser.find_element_by_id("text")
    email.send_keys(username)
    passw=browser.find_element_by_id("password")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)

#elem=browser.find_element_by_link_text('Log in')
#elem.click()

    
def fbLogin():
    url="https://www.facebook.com/"
    browser.get(url)
    email=browser.find_element_by_id("email")
    email.send_keys(username)
    passw=browser.find_element_by_id("pass")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)

def lmsLogin():
    url="http://lms.bennett.edu.in/"
    browser.get(url)
    email=browser.find_element_by_id("inputName")
    email.send_keys(username)
    passw=browser.find_element_by_id("inputPassword")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)

lmsLogin()
