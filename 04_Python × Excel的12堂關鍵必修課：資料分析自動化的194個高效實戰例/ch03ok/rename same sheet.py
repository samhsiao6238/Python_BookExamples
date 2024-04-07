from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
location = Path('更新同名工作表')
files = location.glob('*.xls*')
for i in files:
    wb = app.books.open(i)
    ws = wb.sheets
    for j in ws:
        if j.name == '第一組':
            j.name = '第一小隊'
            break
    wb.save()
    wb.close()
app.quit()
