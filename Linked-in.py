import os,random,sys,time
from selenium import webdriver
from bs4 import BeautifulSoup


browser=webdriver.Chrome()
browser.get("https://www.linkedin.com/login")

elementID=browser.find_element_by_id('username')
elementID.send_keys('<your username>')

elementID=browser.find_element_by_id('password')
elementID.send_keys('<your password>')
elementID.submit()

searchElement=browser.find_element_by_xpath('//*[@id="ember16"]/input')
searchElement.send_keys('iiec rise')
# searchElement=browser.find_element_by_xpath('//*[@id="ember1623"]')
searchElement=browser.find_element_by_xpath('//*[@id="ember14"]/div[2]').click()
# searchElement=browser.find_element_by_xpath('//*[@id="ember401"]').click()
# browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page 

browser.execute_script("window.scrollTo(0, window.scrollY + 200)")


likeElement=browser.find_element_by_xpath('//*[@id="ember264"]/span/div/span').click()


# //*[@id="ember264"]

# searchElement.submit()
