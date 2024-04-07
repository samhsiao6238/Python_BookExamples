# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[16800,20000,21600,25400,12800,20000,25000,14600,32800,25400,18000,10600]
plt.plot(x, y, marker='.')
plt.xlabel('月份')
plt.ylabel('薪水')
plt.title('每月薪水收入折線圖')
plt.grid(visible=True, axis='both', color='r', linestyle='dotted', linewidth=2)
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
