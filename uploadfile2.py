from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://testautomationpractice.blogspot.com/')
driver.switch_to.frame('frame-one1434677811')
button = driver.find_element_by_xpath( '//*[@name="RESULT_FileUpload-10"]' )
driver.execute_script('arguments[0].scrollIntoView();', button)
button.send_keys('C://Users/kajal.t/Pictures/minions/')