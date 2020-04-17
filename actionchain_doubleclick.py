import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://testautomationpractice.blogspot.com/')

copy = driver.find_element_by_xpath('//*[contains(text(),"Copy Text")]')
actions = ActionChains(driver)
actions.double_click(copy).perform()

time.sleep(3)
driver.quit()