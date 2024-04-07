import pandas as pd
data = pd.read_excel('銷售表.xlsx', sheet_name='總表')
condition1 = (data['產品名稱'] == '轉速表') & (data['銷售數量'] >= 50)
condition2 = (data['產品名稱'] == '轉速表') | (data['銷售數量'] >= 50)
data1 = data[condition1]
data2 = data[condition2]
data1.to_excel('銷售表1.xlsx', sheet_name='與條件篩選', index=False)
data2.to_excel('銷售表2.xlsx', sheet_name='或條件篩選', index=False)
