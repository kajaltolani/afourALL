import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.implicitly_wait(5)      #implicit wait
driver.maximize_window()
driver.get('https://www.expedia.com')
driver.find_element(By.ID,'tab-flight-tab-hp').click()
time.sleep(2)      #Python wait function

'''from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as object1
driver.wait1 = WebDriverWait(driver,10)
element = driver.wait1.until(object1.presence_of_element_located((By.ID,'flight-type-multi-dest-label-hp-flight')))
driver.find_element(By.ID,'flight-type-multi-dest-label-hp-flight').click()

driver.get('https://www.extrahop.com')
print(driver.title)

driver.wait = WebDriverWait(driver,5)
driver.wait.until(object1.element_to_be_clickable((By.ID,'wistia_29.thumb_container')))
driver.find_element_by_id('wistia_29.thumb_container').click()'''

driver.get('http://newtours.demoaut.com/mercuryregister.php')
ele= driver.find_elements(By.CSS_SELECTOR("input['maxlength'='64']"))
print(len(ele))

time.sleep(2)
driver.quit()