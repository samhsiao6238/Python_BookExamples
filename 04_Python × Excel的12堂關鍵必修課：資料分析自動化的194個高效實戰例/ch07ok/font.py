import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('產品銷售.xlsx')
ws = wb.sheets[0]
title = ws.range('A1:E1')
title.font.name = '標楷體'
title.font.size = 16
title.font.bold = True
title.font.color = (255, 0, 0)
title.color = (0, 255, 0)
content = ws.range('A2:E6')
content.font.name = '標楷體'
content.font.size = 12
wb.save('產品銷售ok.xlsx')
wb.close()
app.quit()
