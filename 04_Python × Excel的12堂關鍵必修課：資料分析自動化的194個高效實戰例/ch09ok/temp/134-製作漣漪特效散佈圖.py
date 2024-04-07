import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import EffectScatter
data = pd.read_excel('客戶滿意度表.xlsx', sheet_name='Sheet1')
x = data['收貨天數(天)']
y = data['客戶滿意度']
chart = EffectScatter()
chart.add_xaxis(x)
chart.add_yaxis(series_name='收貨天數(天),客戶滿意度', y_axis=y, label_opts=opts.LabelOpts(is_show=False), symbol_size=15)
chart.set_global_opts(title_opts=opts.TitleOpts(title='收貨天數與客戶滿意度散佈圖'), yaxis_opts=opts.AxisOpts(type_='value', name='客戶滿意度', name_location='middle', name_gap=40), xaxis_opts=opts.AxisOpts(type_='value', name='收貨天數(天)', name_location='middle', name_gap=40), tooltip_opts=opts.TooltipOpts(trigger='item', formatter='{a}:{c}'))
chart.render('散佈圖.html')
