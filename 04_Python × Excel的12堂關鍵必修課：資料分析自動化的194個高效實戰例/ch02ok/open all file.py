import xlwings as xw
from pathlib import Path
app = xw.App(visible=True, add_book=False)
location = Path('border')
files= location.glob('*.xls*')
for i in files:
    app.books.open(i)
