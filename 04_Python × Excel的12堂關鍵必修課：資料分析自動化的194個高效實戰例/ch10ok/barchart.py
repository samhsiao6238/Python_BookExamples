from pyecharts.charts import Bar
x = ['東南亞語言', '日韓語言', '歐語系列', '英語系列', '外國人學中文']
y = [580000, 640000, 720000, 1080000, 480000]
chart = Bar()
chart.add_xaxis(x)
chart.add_yaxis('業務金額', y)
chart.render('直條圖.html')
