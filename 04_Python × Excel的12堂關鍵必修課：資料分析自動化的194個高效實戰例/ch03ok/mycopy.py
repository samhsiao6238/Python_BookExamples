import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb1 = app.books.open('複製1.xlsx')
wb2 = app.books.open('複製2.xlsx')
ws1 = wb1.sheets[0]
ws2 = wb2.sheets[1]
ws1.copy(after=ws2)
wb2.save('複製2ok.xlsx')
app.quit()
