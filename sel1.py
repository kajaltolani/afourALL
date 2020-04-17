from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://testautomationpractice.blogspot.com/')
x = driver.title
print(x)
print(driver.current_url)
print(driver.page_source)
