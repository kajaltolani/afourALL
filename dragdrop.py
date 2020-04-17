import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()

driver.get('https://jqueryui.com/draggable/#sortable')
driver.switch_to.frame(driver.find_element_by_css_selector('.demo-frame'))
# source=driver.find_element_by_id('draggable')

sources = driver.find_elements_by_xpath('//*[@class="ui-state-default ui-sortable-handle"]')
# for row in sources:
