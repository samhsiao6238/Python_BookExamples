import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(10, 5))
data = pd.read_excel('線上軟體.xlsx')
n = data['課程名稱']
x = data['授權數(人)']
y = data['總額(元)']
z = data['利潤(%)']
plt.scatter(x, y, s=z * 6000, color='g', marker='o')
plt.xlabel('授權數(人)', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 12}, labelpad=2)
plt.ylabel('總額(元)', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 12}, labelpad=2)
plt.title('數位新知創新學院', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 20}, loc='center')
for a, b, c in zip(x, y, n):
    plt.text(x=a, y=b, s=c, ha='center', va='center', fontsize=12, color='w')
plt.xlim(0, 100)
plt.ylim(0, 30000)
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
