from openpyxl import load_workbook
wb = load_workbook('刪除空白欄.xlsx')
ws = wb['Sheet1']
ws.delete_cols(3, 1)
wb.save('刪除空白欄ok.xlsx')
