import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('工作表名稱.xlsx')
ws = wb.sheets
lists = []
for i in ws:
    name = i.name
    lists.append(name)
for i in lists:
    print(i)
wb.close()
app.quit()
