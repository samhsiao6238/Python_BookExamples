import xlwings as xw
app = xw.App(visible=True, add_book=False)
location = '書籍資訊.xlsx'
app.books.open(location)
