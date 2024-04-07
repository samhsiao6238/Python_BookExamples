from openpyxl import load_workbook
wb = load_workbook('隱藏欄.xlsx')
ws= wb['Sheet1']
ws.column_dimensions.group('C', 'D', hidden=True)
wb.save('隱藏欄ok.xlsx')
