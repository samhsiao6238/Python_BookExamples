import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
figure = plt.figure(figsize=(10, 4))
data = pd.read_excel('各月銷售數量表.xlsx', sheet_name='1月')
x = data['配件名稱']
y = data['銷售數量']
plt.bar(x, y, width=0.5, align='center', color='k')
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('各月銷售數量表.xlsx')
worksheet = workbook.sheets['1月']
worksheet.pictures.add(figure, left=500)
workbook.save('各月銷售數量表1.xlsx')
workbook.close()
app.quit()
