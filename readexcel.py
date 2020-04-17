from selenium import webdriver
import time
import openpyxl

'''driver = webdriver.Chrome(executable_path='D:\Drivers\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.india.gov.in/user/register')'''
excel_data_file = 'testdata/test123.xlsx'
workbook = openpyxl.load_workbook(excel_data_file)
sheet = workbook.active

rows = sheet.max_row
print(rows)
'''dict1 = {}

#for row in range(1, sheet.nrows):
username = sheet.cell_value(1,2)
print(username)'''






