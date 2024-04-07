import matplotlib.pyplot as plt

x = [1.5, 3.8, 5.8, 8.6, 12]
y = [3, 4.6, 6.8, 8.4, 10.6]

fig = plt.figure()

pic = fig.add_subplot(1, 1, 1)

pic.scatter(x, y, s=250, alpha=0.4, linewidths=2.5, c='#00FF00', edgecolors='red')
plt.show() 
