from openpyxl import load_workbook
from openpyxl.styles import Alignment

wb = load_workbook('alignment.xlsx')
sh=wb.active

#設定欄寬
width={"A":40,"B":20,"C":20,"D":20 }
for col_name in width:
    sh.column_dimensions[col_name].width=width[col_name]

head=['A','B','C','D']
for ch in head:
    sh[ch+'1'].alignment=Alignment(horizontal="center",vertical="bottom")

for i in range(2,9): 
    sh['A'+str(i)].alignment=Alignment(horizontal="distributed",vertical="bottom")

for i in range(2,9): 
    sh['B'+str(i)].alignment=Alignment(horizontal="center",vertical="center")

for i in range(2,9): 
    sh['C'+str(i)].alignment=Alignment(horizontal="right",vertical="top")

for i in range(2,9): 
    sh['D'+str(i)].alignment=Alignment(horizontal="left",vertical="bottom")

wb.save('alignment_ok.xlsx')
