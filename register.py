import time
import sys

from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.get('https://www.india.gov.in/user/register')

uname=driver.find_element_by_xpath('//*[@id="edit-name"]')
uname.send_keys('Kajal19')

mail=driver.find_element_by_xpath('//*[@id="edit-mail"]')
mail.send_keys('kajal.tolani@afourtech.com')

pswd1=driver.find_element_by_xpath('//*[@id="edit-pass-pass1"]')
pswd1.send_keys('@four123')
pswd2=driver.find_element_by_xpath('//*[@id="edit-pass-pass2"]')
pswd2.send_keys('@four123')

confirmation=driver.find_element_by_xpath('//*[@class="password-confirm"]')

try:
    assert confirmation.text == 'Passwords match: yes'
except:
    print('Passwords do not match')
    sys.exit()

fname=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-first-name-und-0-value"]')
fname.send_keys('Kajal')

lname=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-last-name-und-0-value"]')
lname.send_keys('Tolani')

country=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-country-und"]')
country.click()

one=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-country-und"]/*[@value="166214"]')
one.click()

pin=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-pin-code-und-0-value"]')
pin.send_keys('422401')

edu=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-education-und"]')
edu.click()

two=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-education-und"]/*[@value="Vocational"]')
two.click()

checkbox=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-subscribe-to-our-newslett-und-yes"]')
print('Checkbox checked? : ',checkbox.is_selected())
checkbox.click()
print('Checkbox checked? : ',checkbox.is_selected())

driver.find_element_by_xpath('//*[@id="edit-submit"]').click()

time.sleep(10)
driver.quit()