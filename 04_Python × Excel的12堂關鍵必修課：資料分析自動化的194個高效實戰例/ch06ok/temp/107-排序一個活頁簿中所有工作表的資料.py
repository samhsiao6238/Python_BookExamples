import xlwings as xw
import pandas as pd
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('各月銷售數量表.xlsx')
worksheet = workbook.sheets
for i in worksheet:
    data = i.range('A1').expand('table').options(pd.DataFrame).value
    result = data.sort_values(by='銷售數量', ascending=False)
    i.range('A1').value = result
workbook.save('各月銷售數量表1.xlsx')
workbook.close()
app.quit()
