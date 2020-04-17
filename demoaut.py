import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:\Drivers\chromedriver.exe")
driver.get("http://newtours.demoaut.com")
driver.maximize_window()
time.sleep(2)
print(driver.current_url)
print(driver.title)

lnks=driver.find_elements_by_tag_name('a')
print(len(lnks))

for ele in lnks:
    print(ele.text)

driver.find_element_by_partial_link_text('Salon Travel').click()
driver.back()

'''u_name=driver.find_element_by_name("userName")
print(u_name.is_displayed())
print(u_name.is_enabled())

pwd=driver.find_element_by_name("password")
print(pwd.is_displayed())
print(pwd.is_enabled())

u_name.send_keys('mercury')
pwd.send_keys('mercury')
driver.find_element_by_name('login').click()
print('login successful')

next=driver.current_url
print(next)

rad1=driver.find_element_by_css_selector('input[value=roundtrip]')
print(rad1.is_displayed())
print(rad1.is_enabled())

rad2=driver.find_element_by_css_selector('input[value=oneway]')
print(rad2.is_displayed())
print(rad2.is_enabled())
print(rad2.is_selected())


time.sleep(2)
driver.find_element_by_link_text('SIGN-OFF').click()
print(driver.current_url)
print('Logout successful')

driver.find_element_by_link_text('registration form').click()
form=driver.current_url
print(form)

#ONE-TIME: fill form
driver.find_element_by_name('firstName').send_keys('Kajal')
driver.find_element_by_name('lastName').send_keys('T')
driver.find_element_by_name('phone').send_keys('1234567890')
driver.find_element_by_id('userName').send_keys('kt@gmail.com')
driver.find_element_by_name('address1').send_keys('AFourtech')
driver.find_element_by_name('address2').send_keys('Bavdhan')
driver.find_element_by_name('city').send_keys('Pune')
driver.find_element_by_name('state').send_keys('Mh')
driver.find_element_by_name('postalCode').send_keys('411021')

s1=Select(driver.find_element_by_name('country'))       #Select is a class, create its object and call in next line
s1.select_by_visible_text('INDIA')

driver.find_element_by_name('email').send_keys('kajalt')
driver.find_element_by_name('password').send_keys('@four123')
driver.find_element_by_name('confirmPassword').send_keys('@four123')
time.sleep(15)      #time to check entered input
driver.find_element_by_name('register').click()
'''

time.sleep(2)
driver.quit()