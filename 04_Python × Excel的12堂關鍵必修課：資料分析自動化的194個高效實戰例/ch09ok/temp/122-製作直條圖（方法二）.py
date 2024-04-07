from pyecharts.charts import Bar
x = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
y = [100, 90, 88, 70, 66, 50, 40, 55, 56, 88, 95, 98]
chart = Bar()
chart.add_xaxis(x)
chart.add_yaxis('銷售量', y)
chart.render('直條圖.html')
