import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 5))
data = pd.read_excel('各月銷售額統計表.xlsx', sheet_name='工作表1')
x = data['月份']
y1 = data['銷售額(萬元)']
y2 = data['同比增長率']
plt.bar(x, y1, color='y', label='銷售額(萬元)')
plt.legend(loc='upper left', fontsize=12)
plt.twinx()
plt.plot(x, y2, color='r', linewidth='3', label='同比增長率')
plt.legend(loc='upper right', fontsize=10)
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
