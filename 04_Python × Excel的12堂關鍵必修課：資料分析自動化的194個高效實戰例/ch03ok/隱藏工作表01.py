import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('4種軟體品項.xlsx')
ws = wb.sheets
for i in ws:
    if i.name == '西班牙語':
        i.visible = False
wb.save()
wb.close()
app.quit()
