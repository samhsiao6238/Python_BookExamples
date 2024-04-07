import pyecharts.options as opts
from pyecharts.charts import Liquid
az = 78.9
moderna=91.1
bnt=95.7
mvc=93.6
base = 100
chart = Liquid()
chart.set_global_opts(title_opts=opts.TitleOpts(title='18-64歲疫苗保護中重症效力分析', pos_left='center'))
chart.add(series_name='AZ', data=[az / base], shape='circle', center=['20%', '50%'])
chart.add(series_name='莫德納', data=[moderna / base], shape='circle', center=['44%', '50%'])
chart.add(series_name='輝瑞', data=[bnt / base], shape='circle', center=['60%', '50%'])
chart.add(series_name='高端', data=[mvc / base], shape='circle', center=['80%', '50%'])
chart.render('水球圖.html')
