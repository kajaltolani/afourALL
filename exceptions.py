from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.gmail.com')
try:
    driver.find_element_by_id('identifierId').click()
    driver.find_element_by_id('identifierId').send_keys('kajal.tolani@afourtech.com')
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
    time.sleep(2)

    driver.find_element_by_name('password').click()
    time.sleep(2)

    driver.find_element_by_name('password').send_keys("kajKAJ1908$*")
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
    time.sleep(2)
    print('Login successful')
except NoSuchElementException as exception:
    print('element not found')
finally:
    driver.quit()