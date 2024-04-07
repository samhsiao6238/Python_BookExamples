import xlwings as xw
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('訂單表3.xlsx')
worksheet = workbook.sheets[0]
row_num = worksheet.range('A1').expand('table').last_cell.row
worksheet.range(f'B2:B{row_num}').number_format = 'yyyy年m月d日'
worksheet.range(f'D2:D{row_num}').number_format = '$#,##0'
worksheet.range(f'E2:E{row_num}').number_format = '$#,##0'
worksheet.range(f'G2:G{row_num}').number_format = '$#,##0.00'
worksheet.range(f'H2:H{row_num}').number_format = '$#,##0.00'
worksheet.range(f'I2:I{row_num}').number_format = '$#,##0.00'
workbook.save('訂單表4.xlsx')
workbook.close()
app.quit()
