import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('國小.xlsx')
ws = wb.sheets['國小']
ws.api.PageSetup.Zoom = 60
ws.api.PrintOut(Copies=1, ActivePrinter='Microsoft Print to PDF', Collate=True)
wb.close()
app.quit()
