from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
location = Path('全部軟體')
files = location.glob('*.xls*')
for i in files:
    wb = app.books.open(i)
    ws = wb.sheets
    for j in ws:
        if j.name == '西班牙語':
            j.visible = False
    wb.save()
    wb.close()
app.quit()
