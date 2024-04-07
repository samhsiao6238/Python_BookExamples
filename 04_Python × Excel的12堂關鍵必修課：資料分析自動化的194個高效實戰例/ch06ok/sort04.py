import pandas as pd
import xlwings as xw
from pathlib import Path
app = xw.App(visible=False, add_book=False)
location = Path('人事室')
files = location.glob('*.xls*')
for i in files:
    wb = app.books.open(i)
    ws = wb.sheets['第三次']
    info = ws.range('A1').expand('table').options(pd.DataFrame).value
    after = info.sort_values(by='平均成績', ascending=False)
    ws.range('A1').value = after
    wb.save()
    wb.close()
app.quit()
