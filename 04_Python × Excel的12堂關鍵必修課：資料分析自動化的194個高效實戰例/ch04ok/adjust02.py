import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('書籍訂單.xlsx')
ws = wb.sheets[0]
target = ws.range('A1').expand('table')
target.column_width = 20
target.row_height = 30
wb.save('書籍訂單ok.xlsx')
wb.close()
app.quit()
