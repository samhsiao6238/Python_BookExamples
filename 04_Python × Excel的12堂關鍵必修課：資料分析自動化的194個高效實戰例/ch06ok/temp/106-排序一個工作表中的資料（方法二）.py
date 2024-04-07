import xlwings as xw
import pandas as pd
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('銷售表.xlsx')
worksheet = workbook.sheets['總表']
data = worksheet.range('A1').expand('table').options(pd.DataFrame).value
result = data.sort_values(by='利潤', ascending=False)
worksheet.range('A1').value = result
workbook.save('銷售表1.xlsx')
workbook.close()
app.quit()
