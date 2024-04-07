import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('調整價格.xlsx')
ws = wb.sheets[0]
data = ws.range('A2').expand('table').value
for i, j in enumerate(data):
    data[i][1] = j[1]+30
ws.range('A2').expand('table').value = data
wb.save('調整價格ok.xlsx')
wb.close()
app.quit()
