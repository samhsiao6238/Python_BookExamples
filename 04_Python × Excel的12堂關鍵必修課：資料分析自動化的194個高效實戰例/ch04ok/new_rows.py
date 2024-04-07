import xlwings as xw
app = xw.App(visible=False, add_book=False)
temprows = [['網路行銷', '420', '500', '0.9',' 189000']]
wb = app.books.open('書籍訂單.xlsx')
ws = wb.sheets['工作表1']
data = ws.range('A1').expand('table')
num = data.shape[0]
ws.range(num + 1, 1).value = temprows
wb.save('書籍訂單(新增列).xlsx')
wb.close()
app.quit()
