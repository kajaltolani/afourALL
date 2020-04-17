import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://unixpapa.com/js/testmouse.html')

click = driver.find_element_by_xpath('//*[contains(text(),"click here to test")]')
clear = driver.find_element_by_link_text('click here to clear')
actions = ActionChains(driver)
actions.context_click(click).context_click(click).perform()
time.sleep(2)
clear.click()
time.sleep(2)
driver.quit()