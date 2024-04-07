import xlwings as xw
app = xw.App(visible=False, add_book=False)
num=3
for i in range(num):
    wb = app.books.add()
    wb.save(f'E:\\example\\成績單{i+1}.xlsx')
    wb.close()
app.quit()

