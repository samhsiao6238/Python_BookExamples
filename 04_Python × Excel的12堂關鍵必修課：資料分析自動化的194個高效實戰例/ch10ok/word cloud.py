import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import WordCloud
data = pd.read_excel('產品銷售.xlsx', sheet_name='工作表1')
employee = data['業務人員']
money = data['銷售額(仟元)']
data1 = [i for i in zip(employee, money)]
pic = WordCloud()
pic.add('銷售額(仟元)', data_pair=data1, shape='triangle', word_size_range=[10, 60])
pic.set_global_opts(title_opts=opts.TitleOpts(title='業務人員業績貢獻分析',
                      title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
                      tooltip_opts=opts.TooltipOpts(is_show=True))
pic.render('文字雲.html')
