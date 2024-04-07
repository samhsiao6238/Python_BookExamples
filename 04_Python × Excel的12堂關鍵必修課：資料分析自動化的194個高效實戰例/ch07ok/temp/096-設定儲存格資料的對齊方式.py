import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('訂單表1.xlsx')
worksheet = workbook.sheets[0]
header = worksheet.range('A1:I1')
header.api.HorizontalAlignment = -4108
header.api.VerticalAlignment = -4108
data = worksheet.range('A2').expand('table')
data.api.HorizontalAlignment = -4152
data.api.VerticalAlignment = -4108
workbook.save('訂單表2.xlsx')
workbook.close()
app.quit()
