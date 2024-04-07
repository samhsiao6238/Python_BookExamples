from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb1 = app.books.open('teacher.xlsx')
ws1 = wb1.sheets['教師總表']
location = Path('批次複製工作表')
files = location.glob('*.xls*')
for i in files:
    wb2 = app.books.open(i)
    ws2 = wb2.sheets[0]
    ws1.copy(before=ws2)
    wb2.save()
app.quit()
