from xlrd import open_workbook
xls=open_workbook('name.xls')
sheet1 = xls.sheet_by_index(0)
sum = 0
for i in range(20):
	sum = sum + sheet1.cell(i,0).value
print sum