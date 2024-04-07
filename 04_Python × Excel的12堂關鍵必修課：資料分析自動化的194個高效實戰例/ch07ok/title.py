import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('在職訓練.xlsx')
ws = wb.sheets[0]
title = ws.range('A1:G1')
title.merge()
title.font.name = '標楷體'
title.row_height = 40
title.font.bold = True
title.font.size = 24
title.api.HorizontalAlignment = -4108
title.api.VerticalAlignment = -4108
wb.save('在職訓練ok.xlsx')
wb.close()
app.quit()
