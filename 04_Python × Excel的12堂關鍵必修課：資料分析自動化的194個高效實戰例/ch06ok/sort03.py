import xlwings as xw
import pandas as pd
app = xw.App(visible=False, add_book=False)
wb = app.books.open('教育訓練多工作表.xlsx')
ws = wb.sheets
for i in ws:
    info = i.range('A1').expand('table').options(pd.DataFrame).value
    after = info.sort_values(by='平均成績', ascending=False)
    i.range('A1').value = after
wb.save('教育訓練多工作表ok.xlsx')
wb.close()
app.quit()
