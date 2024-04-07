import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('教育訓練_多工作表.xlsx')
ws = wb.sheets
for num in ws:
    num.autofit()
wb.save('教育訓練_多工作表ok.xlsx')
wb.close()
app.quit()
