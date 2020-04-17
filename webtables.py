from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('http://testautomationpractice.blogspot.com/')
driver.execute_script('window.scrollBy(0, 1800)')
time.sleep(2)
rows = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr'))
print(rows)
columns = len(driver.find_elements_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th'))
print(columns)

for r in range(2,rows+1):
    for c in range(1,columns+1):
        value = driver.find_element_by_xpath('//*[@id="HTML1"]/div[1]/table/tbody/tr['+str(r)+']/td['+str(c)+']').text
        print(value,end="        ")
    print()

driver.save_screenshot('D:\Screenshots\screenshot1.jpeg')
driver.quit()