import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('保護工作表.xlsx')
ws = wb.sheets['產品資訊']
ws.api.Protect(Password='0000', Contents=True)
wb.save('保護工作表ok.xlsx')
wb.close()
app.quit()
