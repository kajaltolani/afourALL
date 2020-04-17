import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.gmail.com')

email = driver.find_element_by_id('identifierId')
email.click()
email.send_keys('kajal.tolani@afourtech.com')
time.sleep(2)

next_email = driver.find_element_by_xpath('//*[@class="RveJvd snByac"]')
next_email.click()
time.sleep(2)

pwd = driver.find_element_by_name('password')
pwd.click()
pwd.send_keys("kajKAJ1908$*")
time.sleep(2)

next_pwd = driver.find_element_by_xpath('//*[@id="passwordNext"]')
next_pwd.click()
time.sleep(2)
print('Login successful')

acc_button = driver.find_element_by_xpath('//*[@class="gb_ia gb_Dg gb_i"]')
acc_button.click()
time.sleep(2)

sign_out = driver.find_element_by_xpath('//*[@id="gb_71"]')
sign_out.click()
time.sleep(2)
print('Logout successful')

driver.quit()