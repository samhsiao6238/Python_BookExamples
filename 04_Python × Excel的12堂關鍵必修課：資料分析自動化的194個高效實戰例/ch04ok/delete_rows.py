from openpyxl import load_workbook
wb = load_workbook('刪除空白列.xlsx')
ws = wb['Sheet1']
ws.delete_rows(4, 2)
wb.save('刪除空白列ok.xlsx')
