import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('國小(含標題列).xlsx')
ws = wb.sheets['國小']
ws.api.PageSetup.PrintTitleRows = '$1:$1'
ws.api.PrintOut(Copies=1, ActivePrinter='Microsoft Print to PDF', Collate=True)
wb.close()
app.quit()
