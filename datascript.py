from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
url = driver.get('http://newtours.demoaut.com/')
target_page = driver.find_element_by_link_text('REGISTER')
target_page.click()

first_name = driver.find_element_by_name('firstName')
last_name = driver.find_element_by_name('lastName')
phone = driver.find_element_by_name('phone')
email = driver.find_element_by_name('userName')
