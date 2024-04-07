from pathlib import Path
import xlwings as xw
import pandas as pd
app = xw.App(visible=False, add_book=False)
folder_path = Path('各地區銷售數量')
file_list = folder_path.glob('*.xls*')
for i in file_list:
    workbook = app.books.open(i)
    worksheet = workbook.sheets['銷售數量']
    data = worksheet.range('A1').expand('table').options(pd.DataFrame).value
    result = data.sort_values(by='銷售數量', ascending=False)
    worksheet.range('A1').value = result
    workbook.save()
    workbook.close()
app.quit()
