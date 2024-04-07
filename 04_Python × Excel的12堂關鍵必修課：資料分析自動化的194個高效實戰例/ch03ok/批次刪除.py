from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
folder_path = Path('產品')
file_list = folder_path.glob('*.xls*')
temp = '產品資訊'
for i in file_list:
    wb = app.books.open(i)
    ws = wb.sheets
    for j in ws:
        sheet_name = j.name
        if sheet_name == temp:
            j.delete()
            break
    wb.save()
    wb.close()
app.quit()
