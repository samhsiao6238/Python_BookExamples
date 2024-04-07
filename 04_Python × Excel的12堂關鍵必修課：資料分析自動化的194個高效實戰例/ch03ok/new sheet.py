import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('新增工作表.xlsx')
ws = wb.sheets
add_sheet = '資優生'
lists = []
for i in ws:
    name = i.name
    lists.append(name)
if add_sheet not in lists:
    ws.add(name=add_sheet)
wb.save('新增工作表ok.xlsx')
wb.close()
app.quit()
