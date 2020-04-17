from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://selenium.dev/selenium/docs/api/java/index.html')
driver.switch_to.frame('packageListFrame')
pck = driver.find_element_by_link_text('org.openqa.selenium')
time.sleep(3)
pck.click()

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')
time.sleep(2)
cls = driver.find_element_by_link_text('WebDriver')
cls.click()

driver.switch_to.default_content()

driver.switch_to.frame('classFrame')
time.sleep(2)
tab = driver.find_element_by_link_text('DEPRECATED')
tab.click()

time.sleep(5)
driver.quit()