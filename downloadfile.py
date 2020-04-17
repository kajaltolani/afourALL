from selenium import webdriver
import time

options = webdriver.ChromeOptions()

options.add_argument("download.default_directory=C:/Users/kajal.t/Documents/ExtraHop/Export")

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe',options=options)

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()
time.sleep(3)

driver.find_element_by_id('textbox').send_keys('testdata')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()
