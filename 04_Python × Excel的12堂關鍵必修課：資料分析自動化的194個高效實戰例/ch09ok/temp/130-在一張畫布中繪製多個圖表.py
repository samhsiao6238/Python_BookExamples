import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
x = ['上海', '台北', '首爾', '香港', '京都', '馬尼拉', '雅加達']
y = [120, 150, 88, 70, 96, 50, 40]
plt.subplot(2, 2, 1)
plt.bar(x, y, width=0.5, align='center', color='r')
plt.subplot(2, 2, 2)
plt.pie(y, labels=x, labeldistance=1.1, autopct='%.2f%%', pctdistance=1.6)
plt.subplot(2, 2, 3)
plt.plot(x, y, color='r', linewidth=3, linestyle='solid')
plt.subplot(2, 2, 4)
plt.stackplot(x, y, color='r')
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
