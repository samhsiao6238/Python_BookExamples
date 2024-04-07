from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
folder_path = Path('多活頁簿')
files = folder_path.glob('*.xls*')
for num1 in files:
    wb = app.books.open(num1)
    ws = wb.sheets
    for num2 in ws:
        num2.autofit()
    wb.save()
    wb.close()
app.quit()
