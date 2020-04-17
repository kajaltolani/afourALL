from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://13.233.127.198/extrahop/')
time.sleep(2)
driver.find_element_by_id('id_username').send_keys('setup')
driver.find_element_by_id('id_password').send_keys('0de88ed33bdffd643')
driver.find_element_by_id('id_loginButton').click()
time.sleep(3)
#driver.find_element_by_id('settings_menu').click()
driver.find_element_by_xpath('//*[@class="c-user-initials c-user-initials--single"]').click()
api = driver.find_element_by_link_text('API Access')
api.click()

'''
driver.get('http://demo.guru99.com/popup.php')
driver.find_element_by_link_text('Click Here').click()
handles=driver.window_handles
driver.switch_to.window(handles[1])
print(driver.current_url)


driver.get('http://hdfcbank.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@class="btn btn-primary login-btn ng-scope"]').click()
driver.find_element_by_xpath('//*[@class="login-rb"]/value=3')
'''
time.sleep(3)

print(driver.current_window_handle) #parent CDwindow-B4FBDC82E31B0F9AC31EED69759BA1C8
handles = driver.window_handles  #returns handles of all open windows
print(handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.switch_to.window(handles[1])
driver.close()
