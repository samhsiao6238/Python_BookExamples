import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb = app.books.open('旅遊.xlsx')
wb.api.Password = '0000'
#wb.api.Password = ''  #將密碼設定為空字串可以取消密碼保護
wb.save()
wb.close()
app.quit()
