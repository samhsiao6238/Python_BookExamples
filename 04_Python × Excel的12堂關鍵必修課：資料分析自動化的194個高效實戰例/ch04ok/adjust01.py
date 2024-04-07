import xlwings as xw
app = xw.App(visible=False, add_book=False)
wb= app.books.open('教育訓練.xlsx')
ws = wb.sheets['Sheet1']
ws.autofit()
wb.save('教育訓練ok.xlsx')
wb.close()
app.quit()
