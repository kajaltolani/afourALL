from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://13.233.107.43/extrahop/')

#//*[@id="details-button"]
#//*[@id="proceed-link"]

try:
    driver.find_element_by_xpath('//*[@id="details-button"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
    time.sleep(3)
except:
    pass
finally:
    username = driver.find_element_by_xpath('//*[@id="id_username"]')
    password = driver.find_element_by_xpath('//input[@id="id_password"]')
    login_button = driver.find_element_by_xpath('//input[@id="id_loginButton"]')

    username.send_keys('setup')
    password.send_keys('05281eeb25f1c5ce5')
    login_button.click()

time.sleep(5)
driver.quit()