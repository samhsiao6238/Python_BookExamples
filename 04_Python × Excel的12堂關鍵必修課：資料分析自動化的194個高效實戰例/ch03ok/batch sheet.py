from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
location = Path('新增工作表')
files = location.glob('*.xls*')
new_add = '資優生'
for i in files:
    wb = app.books.open(i)
    ws = wb.sheets
    lists = []
    for j in ws:
        tempname = j.name
        lists.append(tempname)
    if new_add not in lists:
        ws.add(name=new_add)
    wb.save()
    wb.close()
app.quit()
