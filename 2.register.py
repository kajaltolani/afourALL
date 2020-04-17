import time
import sys
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.get('https://www.india.gov.in/user/register')

driver.maximize_window()
driver.implicitly_wait(10)

fname = driver.find_element_by_xpath('//*[@id="edit-profile-main-field-first-name-und-0-value"]')
fname.send_keys('kajal')

#cnfpwd= driver.find_element_by_xpath('//*[@id="edit-pass-pass2"]')
#cnfpwd.send_keys('newpassword')

country = Select(driver.find_element_by_xpath('//*[@id="edit-profile-main-field-country-und"]'))
country.select_by_visible_text('Germany')
for ele in country.options:
    print(ele.text)
print(len(country.options))

'''one=driver.find_element_by_xpath('//*[@id="edit-profile-main-field-country-und"]/*[@value="166214"]').click()

two = driver.find_elements_by_xpath('//*[@id="edit-profile-main-field-country-und"]/option')
for ele in two:
    print(ele.text)
    if ele.text == 'Greece':
        ele.click()

three = [ele3 for ele3 in two if ele3.text == 'Greece']
three[0].click()'''

pincode = driver.find_element_by_xpath('//*[@id="edit-profile-main-field-pin-code-und-0-value"]')
pincode.send_keys('2342342')

pswd1=driver.find_element_by_xpath('//*[@id="edit-pass-pass1"]')
pswd1.send_keys('@four123')
pswd2=driver.find_element_by_xpath('//*[@id="edit-pass-pass2"]')
pswd2.send_keys('@four123')

confirmation=driver.find_element_by_xpath('//*[@class="password-confirm"]')

try:
    assert confirmation.text == 'Passwords match: yes'
except:
    print('Passwords do not match')
    driver.quit()
    sys.exit()

chckbox = driver.find_element_by_xpath('//*[@id="edit-profile-main-field-subscribe-to-our-newslett-und-yes"]')
print(chckbox.is_selected())
chckbox.click()
print(chckbox.is_selected())

time.sleep(5)
driver.quit()