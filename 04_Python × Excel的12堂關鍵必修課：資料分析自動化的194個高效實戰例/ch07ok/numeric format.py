import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('數值格式.xlsx')
ws = wb.sheets[0]
end = ws.range('A1').expand('table').last_cell.row
ws.range(f'A2:A{end}').number_format = 'yyyy年m月d日'
ws.range(f'C2:C{end}').number_format = '$#,##0'
ws.range(f'E2:E{end}').number_format = '$#,##0.00'
wb.save('數值格式ok.xlsx')
wb.close()
app.quit()
