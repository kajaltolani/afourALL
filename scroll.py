from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://testautomationpractice.blogspot.com/')

'''#1. scroll to pixel
driver.execute_script('window.scrollBy(0,1000)')'''

#2. Scroll until element is visible
flag = driver.find_element_by_id('animals')
driver.execute_script('arguments[0].scrollIntoView();',flag)

#3. Scroll till end of page
#driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
