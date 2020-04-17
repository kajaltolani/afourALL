import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')

driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()
admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/*["Admin"]')
usermngmnt = driver.find_element_by_id('menu_admin_UserManagement')
user = driver.find_element_by_id('menu_admin_viewSystemUsers')
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermngmnt).move_to_element(user).click().perform()

time.sleep(3)
driver.quit()