import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('國小.xlsx')
ws = wb.sheets['國小']
target = ws.range('A1:C20')
target.api.PrintOut(Copies=1, ActivePrinter='Microsoft Print to PDF', Collate=True)
wb.close()
app.quit()
