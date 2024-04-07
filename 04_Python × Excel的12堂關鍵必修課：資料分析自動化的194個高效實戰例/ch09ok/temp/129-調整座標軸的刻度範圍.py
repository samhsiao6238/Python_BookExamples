import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
x = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
y = [100, 90, 88, 70, 66, 50, 40, 55, 56, 88, 95, 98]
plt.plot(x, y, color='k', linewidth=3, linestyle='solid')
plt.title(label='銷售量趨勢圖', fontdict={'family': 'Microsoft Jhenghei', 'color': 'k', 'size': 25}, loc='center')
plt.ylim(20, 120)
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
