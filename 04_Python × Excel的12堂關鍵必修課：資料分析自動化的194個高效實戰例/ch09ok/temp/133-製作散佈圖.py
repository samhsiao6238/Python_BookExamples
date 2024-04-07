import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
figure = plt.figure(figsize=(10, 4))
data = pd.read_excel('客戶滿意度表.xlsx', sheet_name='Sheet1')
x = data['收貨天數(天)']
y = data['客戶滿意度']
plt.scatter(x, y, s=100, marker='o', color='k')
x1 = x.to_numpy().reshape(-1, 1)
model = linear_model.LinearRegression().fit(x1, y)
y1 = model.predict(x1)
plt.plot(x, y1, color='k', linewidth='3', linestyle='solid')
plt.title(label='收貨天數與客戶滿意度關係圖', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 25}, loc='center')
plt.xlabel('收貨天數(天)', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 12}, labelpad=2)
plt.ylabel('客戶滿意度', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 12}, labelpad=2)
plt.xlim(0, 22.5)
plt.ylim(0, 12)
plt.rcParams['axes.unicode_minus'] = False
plt.show()
