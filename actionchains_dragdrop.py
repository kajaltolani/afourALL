import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://testautomationpractice.blogspot.com/')

scroll = driver.find_element_by_xpath('//*[contains(text(),"Drag and Drop")]')
draggable = driver.find_element_by_id('draggable')
droppable = driver.find_element_by_id('droppable')

driver.execute_script('arguments[0].scrollIntoView();',scroll)
actions = ActionChains(driver)
actions.drag_and_drop(draggable,droppable).perform()
time.sleep(2)

Mr_John = driver.find_element_by_xpath('//*[contains(text(),"Mr John")]')
trash = driver.find_element_by_id('trash')

#driver.execute_script('arguments[0],scrollIntoView();',Mr_John)
actions.drag_and_drop(Mr_John,trash).perform()

time.sleep(3)
driver.quit()