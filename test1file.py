import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
#driver = webdriver.Firefox(executable_path='D:\Drivers\geckodriver.exe')
#driver = webdriver.Ie(executable_path='D:\Drivers\IEDriverServer.exe')

driver.set_page_load_timeout(10)
driver.get('https://13.126.51.129')
driver.maximize_window()
driver.refresh()

#title, URL
print('Title: ',driver.title)
print('Current URL: ', driver.current_url)

#Login
driver.find_element_by_id('id_username').send_keys('setup')
driver.find_element_by_id('id_password').send_keys('0f4e7352eb9995241')
driver.find_element_by_id('id_loginButton').click()
print('Login successful')

time.sleep(2)
driver.find_element_by_css_selector('button.c-dock__new-dashboard.Button').click()
one=driver.find_element_by_css_selector('input.qa-properties__name.c-input.c-field')    #dashboard name field
print(one.is_displayed())
print(one.is_enabled())
driver.find_element_by_css_selector('button.Button.qa-properties__cancel').click()


'''
time.sleep(3)
driver.get('https://www.google.com')
print('title: ', driver.title)

time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()

driver.find_element_by_class_name("fa.fa-stack-1x.fa-exclamation").click()          #system settings gear

#Create new dashboard
driver.implicitly_wait(5)
driver.find_element_by_css_selector('button.c-dock__new-dashboard.Button').click()
driver.find_element_by_css_selector('input.qa-properties__name.c-input.c-field').clear()
driver.find_element_by_css_selector('input.qa-properties__name.c-input.c-field').send_keys('AFourtech')
driver.implicitly_wait(5)
driver.find_element_by_css_selector('button.Button.Button-highlight.qa-properties__save').click()
print('New dashboard created successfully')
'''

time.sleep(2)
driver.quit()