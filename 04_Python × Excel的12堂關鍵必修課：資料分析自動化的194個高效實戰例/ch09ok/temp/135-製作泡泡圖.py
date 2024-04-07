import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(10, 5))
data = pd.read_excel('銷售統計表.xlsx', sheet_name='Sheet1')
n = data['產品名稱']
x = data['銷售量(台)']
y = data['銷售額(元)']
z = data['毛利率(%)']
plt.scatter(x, y, s=z * 5000, color='r', marker='o')
plt.xlabel('銷售量(台)', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 12}, labelpad=2)
plt.ylabel('銷售額(元)', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 12}, labelpad=2)
plt.title('銷售量、銷售額與毛利率關係圖', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 20}, loc='center')
for a, b, c in zip(x, y, n):
    plt.text(x=a, y=b, s=c, ha='center', va='center', fontsize=12, color='w')
plt.xlim(20, 100)
plt.ylim(0, 50000)
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
