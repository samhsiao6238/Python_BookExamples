from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
folder_path = Path('全部軟體')
files = folder_path.glob('*.xls*')
types = ['西班牙語', '越語']
for i in files:
    wb = app.books.open(i)
    ws = wb.sheets
    for j in ws:
        if j.name in types:
            j.visible = False
    wb.save()
    wb.close()
app.quit()
