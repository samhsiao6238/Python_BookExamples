import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('轉置.xlsx')
ws = wb.sheets[0]
data = ws.range('A1').expand('table').options(transpose=True).value
ws.clear()
ws.range('A1').expand().value = data
wb.save('轉置ok.xlsx')
wb.close()
app.quit()
