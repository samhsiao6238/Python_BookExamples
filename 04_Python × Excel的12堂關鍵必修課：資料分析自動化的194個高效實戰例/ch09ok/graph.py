import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw
figure = plt.figure(figsize=(10, 4))
data = pd.read_excel('暢銷商品.xlsx', sheet_name='暢銷商品')
x = data['業務人員編號']
y = data['總金額']
plt.bar(x, y, width=0.5, align='center', color='r')
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
app = xw.App(visible=False, add_book=False)
workbook = app.books.open('暢銷商品.xlsx')
worksheet = workbook.sheets['暢銷商品']
worksheet.pictures.add(figure, top=100)
workbook.save('暢銷商品(含圖表).xlsx')
workbook.close()
app.quit()
