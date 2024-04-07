import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('訂單表2.xlsx')
worksheet = workbook.sheets[0]
area = worksheet.range('A1').expand('table')
for i in area:
    for j in range(7, 11):
        i.api.Borders(j).LineStyle = 1
        i.api.Borders(j).Weight = 2
        i.api.Borders(j).Color = xw.utils.rgb_to_int((255, 0, 0))
workbook.save('訂單表3.xlsx')
workbook.close()
app.quit()
