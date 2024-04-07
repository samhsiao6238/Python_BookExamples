import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('更改標籤顏色.xlsx')
ws = wb.sheets
for i in ws:
    if i.name == '產品資訊':
        i.api.Tab.Color = 0+255*256+0*256*256
wb.save('更改標籤顏色ok.xlsx')
wb.close()
app.quit()
