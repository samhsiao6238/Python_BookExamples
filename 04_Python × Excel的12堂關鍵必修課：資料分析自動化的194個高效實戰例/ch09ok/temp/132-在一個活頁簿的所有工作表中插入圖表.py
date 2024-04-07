import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
all_data = pd.read_excel('各月銷售數量表.xlsx', sheet_name=None)
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('各月銷售數量表.xlsx')
worksheet = workbook.sheets
for i in all_data:
    figure = plt.figure(figsize=(10, 4))
    data = all_data[i]
    x = data['配件名稱']
    y = data['銷售數量']
    plt.bar(x, y, width=0.5, align='center', color='k')
    plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
    plt.rcParams['axes.unicode_minus'] = False
    worksheet[i].pictures.add(figure, left=400)
workbook.save('各月銷售數量表1.xlsx')
workbook.close()
app.quit()
