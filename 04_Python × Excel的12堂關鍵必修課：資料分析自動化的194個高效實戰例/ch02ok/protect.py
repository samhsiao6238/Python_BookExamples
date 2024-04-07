import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('單字表.xlsx')
wb.api.Protect(Password='0000', Structure=True, Windows=True)
#wb.api.Unprotect('0000') #此指令是取消活頁簿結構的保護
wb.save()
wb.close()
app.quit()
