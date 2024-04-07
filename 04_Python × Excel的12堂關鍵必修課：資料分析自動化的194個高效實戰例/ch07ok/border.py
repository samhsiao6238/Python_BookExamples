from openpyxl import load_workbook
from openpyxl.styles import Border, Side

wb = load_workbook('border.xlsx')
target=wb.active

s1=Side(style="thick",color="FFFF00")

for rows in target["A1":"C8"]:
    for cell in rows:
        cell.border=Border(left=s1,right=s1,top=s1,bottom=s1)
        
wb.save('border1_ok.xlsx')

s1=Side(style="dashDot",color="FF0000")
for rows in target["A1":"C8"]:
    for cell in rows:
        cell.border=Border(left=s1,right=s1,top=s1,bottom=s1)
        
wb.save('border2_ok.xlsx')

s1=Side(style="slantDashDot",color="00FF00")
for rows in target["A1":"C8"]:
    for cell in rows:
        cell.border=Border(left=s1,right=s1,top=s1,bottom=s1)
        
wb.save('border3_ok.xlsx')

s1=Side(style="hair",color="0000FF")
for rows in target["A1":"C8"]:
    for cell in rows:
        cell.border=Border(left=s1,right=s1,top=s1,bottom=s1)
        
wb.save('border4_ok.xlsx')

s1=Side(style="dashDotDot",color="000000")
for rows in target["A1":"C8"]:
    for cell in rows:
        cell.border=Border(left=s1,right=s1,top=s1,bottom=s1)
        
wb.save('border5_ok.xlsx')
