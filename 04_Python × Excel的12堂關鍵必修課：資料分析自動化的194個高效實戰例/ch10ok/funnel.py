import pyecharts.options as opts
from pyecharts.charts import Funnel
x = ['廣告量', '拜訪人數', '進入產品贖買頁', '支付金額']
y = [100000, 20000, 4500, 1280]
data = [i for i in zip(x, y)]
chart = Funnel()
chart.add(series_name='人數', data_pair=data, label_opts=opts.LabelOpts(is_show=True, position='inside'))
chart.set_global_opts(title_opts = opts.TitleOpts(title='漏斗圖', pos_left='right'), legend_opts=opts.LegendOpts(is_show=True))
chart.render('漏斗圖.html')
