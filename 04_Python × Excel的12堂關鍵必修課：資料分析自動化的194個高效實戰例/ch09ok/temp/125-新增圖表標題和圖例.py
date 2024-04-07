import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
x = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
y = [100, 90, 88, 70, 66, 50, 40, 55, 56, 88, 95, 98]
plt.bar(x, y, width=0.5, align='center', color='k', label='銷售量(台)')
plt.legend(loc='best', fontsize=12)
plt.title(label='銷售量對比圖', fontdict={'family': 'DFKai-SB', 'color': 'k', 'size': 25}, loc='center')
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
