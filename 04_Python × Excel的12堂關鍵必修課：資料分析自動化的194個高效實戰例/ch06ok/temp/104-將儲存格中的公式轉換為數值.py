import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('銷售表公式轉數值.xlsx')
worksheet = workbook.sheets[0]
data = worksheet.range('A1').expand('table').value
worksheet.range('A1').expand('table').value = data
workbook.save('銷售表3.xlsx')
workbook.close()
app.quit()
