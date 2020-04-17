from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.implicitly_wait(10)

alertbox=driver.find_element_by_xpath('//*[@onclick="myFunction()"]')
alertbox.click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(1)
alertbox.click()
message=driver.switch_to.alert.text
print(message)
driver.switch_to.alert.dismiss()

time.sleep(3)
driver.quit()