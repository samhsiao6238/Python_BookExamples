from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
location = Path('E:\\example\\')
files = location.glob('*.xlsx')
for i in files:
    name = str(i.with_suffix('.xls'))
    wb = app.books.open(i)
    wb.api.SaveAs(name, FileFormat=56)
    wb.close()
app.quit()
