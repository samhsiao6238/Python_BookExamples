# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
y = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, y,width=0.5, align='edge', color='r')
for a, b in zip(x, y):
    plt.text(x=a, y=b, s=b, ha='center', va='bottom', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 15})
plt.xlabel('學期', fontdict={'family': 'Microsoft Jhenghei', 'color': 'r', 'size': 14}, labelpad=2)
plt.ylabel('平均分數',fontdict={'family': 'Microsoft Jhenghei', 'color': 'r', 'size': 14}, labelpad=4)
plt.title('大學四年各學期的平均分數')
plt.rcParams['axes.unicode_minus'] = False
plt.show()
