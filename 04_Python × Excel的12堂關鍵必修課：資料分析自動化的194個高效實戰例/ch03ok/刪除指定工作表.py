import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('軟體資訊.xlsx')
ws = wb.sheets
temp = '產品資訊'
for i in ws:
    sheet_name = i.name
    if sheet_name == temp:
        i.delete()
        break
wb.save('軟體資訊ok.xlsx')
wb.close()
app.quit()
