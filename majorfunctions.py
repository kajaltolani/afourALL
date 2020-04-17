import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome( executable_path='D:\Drivers\chromedriver.exe' )
driver.maximize_window()
driver.get( 'http://testautomationpractice.blogspot.com/' )

data = driver.find_element_by_id('draggable').get_attribute()