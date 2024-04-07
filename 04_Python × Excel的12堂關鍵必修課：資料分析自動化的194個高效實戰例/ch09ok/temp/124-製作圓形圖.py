import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
x = ['上海', '台北', '首爾', '香港', '京都', '馬尼拉', '雅加達']
y = [120, 150, 88, 70, 96, 50, 40]
plt.pie(y, labels=x, labeldistance=1.1, autopct='%.2f%%', pctdistance=1.5, counterclock=False, startangle=90, explode=[0.3, 0, 0, 0, 0, 0, 0])
plt.rcParams['font.sans-serif'] = ['Microsoft Jhenghei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
