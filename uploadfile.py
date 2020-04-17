from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

driver=webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.filedropper.com/')
time.sleep(2)
driver.find_element_by_id('uploadFile').send_keys('C:/Users/kajal.t/Videos/ExtraHop/1. print-EDA.flv')
wait=WebDriverWait(driver,15)
wait.until(ec.url_changes)
new=driver.current_url
print(new)
time.sleep(3)
driver.quit()