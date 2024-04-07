import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('汽車銷售.xlsx', sheet_name='工作表1')
plt.figure(figsize=(6, 5))
x = data['月份']
y1 = data['汽車數量']
y2 = data['汽車平均價格']
plt.bar(x, y1, color='b', label='汽車數量(台)')
plt.legend(loc='upper left', fontsize=12)
plt.twinx()
plt.plot(x, y2, color='r', linewidth='3', label='平均價格(萬)')
plt.legend(loc='upper right', fontsize=10)
plt.show()
