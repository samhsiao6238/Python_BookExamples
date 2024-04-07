import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('更名工作表.xlsx')
ws = wb.sheets
for i in ws:
    if i.name == '第一組':
        i.name = '第一小隊'
        break
wb.save('更名工作表ok.xlsx')
wb.close()
app.quit()
