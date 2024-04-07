import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('訂單表5.xlsx')
worksheet = workbook.sheets[0]
title = worksheet.range('A1:I1')
title.merge()
title.font.name = '微軟正黑體'
title.font.size = 18
title.font.bold = True
title.api.HorizontalAlignment = -4108
title.api.VerticalAlignment = -4108
title.row_height = 30
workbook.save('訂單表6.xlsx')
workbook.close()
app.quit()
