import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('訂單表.xlsx')
worksheet = workbook.sheets[0]
header = worksheet.range('A1:I1')
header.font.name = '微軟正黑體'
header.font.size = 10
header.font.bold = True
header.font.color = (255, 255, 255)
header.color = (0, 0, 0)
data = worksheet.range('A2').expand('table')
data.font.name = '微軟正黑體'
data.font.size = 10
workbook.save('訂單表1.xlsx')
workbook.close()
app.quit()
