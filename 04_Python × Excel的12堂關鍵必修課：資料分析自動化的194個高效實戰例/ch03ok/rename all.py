import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('更名工作表.xlsx')
ws = wb.sheets
for i in ws:
    i.name = i.name.replace('組', '小隊')
wb.save('批次命名ok.xlsx')
wb.close()
app.quit()
