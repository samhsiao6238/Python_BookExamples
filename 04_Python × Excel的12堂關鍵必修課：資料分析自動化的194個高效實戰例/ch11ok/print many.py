from pathlib import Path
import xlwings as xw
location = Path('多份統計表')
files = location.glob('*.xls*')
app = xw.App(visible=False, add_book=False)
for i in files:
    wb = app.books.open(i)
    wb.api.PrintOut(Copies=1, ActivePrinter='Microsoft Print to PDF', Collate=True)
    wb.close()
app.quit()
