import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('指考成績.xlsx')
ws = wb.sheets['第一班']
ws.api.PageSetup.CenterVertically = True
ws.api.PageSetup.CenterHorizontally = True
ws.api.PrintOut(Copies=1, ActivePrinter='Microsoft Print to PDF', Collate=True)
wb.close()
app.quit()
