import xlwings as xw
app = xw.App(visible=False, add_book=False)
location = '業績表.xlsx'
wb = app.books.open(location)
ws = wb.sheets
for i in ws:
    new_wb = app.books.add()
    new_ws = new_wb.sheets[0]
    i.copy(before=new_ws)
    new_wb.save('拆分業績表\\{}.xlsx'.format(i.name))
    new_wb.close()
app.quit()
