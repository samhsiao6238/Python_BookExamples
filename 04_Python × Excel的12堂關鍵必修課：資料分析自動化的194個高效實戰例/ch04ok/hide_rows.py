from openpyxl import load_workbook
wb = load_workbook('隱藏列.xlsx')
ws = wb['Sheet1']
ws.row_dimensions.group(2, 14, hidden=True)
wb.save('隱藏列ok.xlsx')
