import xlrd
path = 'testdata/data.xls'

workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_name('Sheet1')
rows = sheet.nrows
cols = sheet.ncols

for r in range(1,rows+1):
    for c in range(0,cols+1):
        print(sheet.cell(r,c).value)
