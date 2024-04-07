from openpyxl import load_workbook
wb = load_workbook('外包錄音費.xlsx')
ws = wb['Sheet1']
ws.insert_rows(4, 2)
wb.save('外包錄音費3.xlsx')
