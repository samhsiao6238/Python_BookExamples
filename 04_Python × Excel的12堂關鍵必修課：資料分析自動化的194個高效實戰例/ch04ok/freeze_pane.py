from openpyxl import load_workbook
wb = load_workbook('授權碼對應表.xlsx')
ws = wb['Sheet1']
ws.freeze_panes = 'B2'
wb.save('授權碼對應表ok.xlsx')
