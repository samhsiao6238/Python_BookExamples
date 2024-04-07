from pathlib import Path
import xlwings as xw
app = xw.App(visible=False, add_book=False)
location = Path('多個密碼')
files = location.glob('*.xls*')
for i in files:
    wb = app.books.open(i)
    wb.api.Password = '0000'
    #wb.api.Password = '' #取消密碼保護
    wb.save()
    wb.close()
app.quit()
