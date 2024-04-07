import xlwings as xw
import pandas as pd
app = xw.App(visible=False, add_book=False)
wb = app.books.open('教育訓練排序.xlsx')
ws = wb.sheets['Sheet1']
info = ws.range('A1').expand('table').options(pd.DataFrame).value
result = info.sort_values(by='平均成績', ascending=False)
ws.range('A1').value = result
wb.save('教育訓練排序2.xlsx')
wb.close()
app.quit()
