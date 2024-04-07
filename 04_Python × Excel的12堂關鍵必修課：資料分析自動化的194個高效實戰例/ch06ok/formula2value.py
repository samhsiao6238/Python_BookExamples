import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('教育訓練.xlsx')
ws = wb.sheets[0]
info = ws.range('A3').expand('table').value
ws.range('A3').expand('table').value = info
wb.save('教育訓練ok.xlsx')
wb.close()
app.quit()
