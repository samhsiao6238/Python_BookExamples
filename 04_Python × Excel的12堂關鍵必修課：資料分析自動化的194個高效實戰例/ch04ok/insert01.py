from openpyxl import load_workbook
wb = load_workbook('外包錄音費.xlsx')
ws = wb['Sheet1']
ws.insert_rows(4, 1)
wb.save('外包錄音費1.xlsx')
