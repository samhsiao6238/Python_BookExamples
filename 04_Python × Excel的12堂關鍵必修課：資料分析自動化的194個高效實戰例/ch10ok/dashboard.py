import pyecharts.options as opts
from pyecharts.charts import Gauge
chart = Gauge()
chart.add(series_name='關鍵績效指標（KPI）', data_pair=[('KPI指標', 63.35)], split_number=10, radius='75%', start_angle=180, end_angle=0,
          is_clock_wise=True, detail_label_opts=opts.GaugeDetailOpts(is_show=False))
chart.set_global_opts(legend_opts=opts.LegendOpts(is_show=True), tooltip_opts=opts.TooltipOpts(is_show=True))
chart.render('儀錶板.html')
