import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.add()
wb.save('成績單.xlsx') #在目前的資料夾新建活頁簿
wb.save(r'E:\example\成績單.xlsx') #指定絕對路徑的活頁簿
#wb.save('E:\\example\\成績單.xlsx') #指定絕對路徑的活頁簿
wb.close()
app.quit()
