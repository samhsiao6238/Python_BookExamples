from openpyxl import load_workbook
wb = load_workbook('外包錄音費.xlsx')
ws = wb['Sheet1']
ws.insert_cols(3)
wb.save('外包錄音費2.xlsx')
