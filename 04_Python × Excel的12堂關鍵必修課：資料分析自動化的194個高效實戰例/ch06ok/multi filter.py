import pandas as pd
data = pd.read_excel('軟體銷售.xlsx', sheet_name='銷售業績')
result1 = (data['產品種類'] == '電腦遊戲') & (data['總金額'] >= 10000000)
data1 = data[result1]
data1.to_excel('軟體銷售01.xlsx', index=False)
result2 = (data['銷售地區'] == '日本') | (data['銷售地區'] == '東南亞')
data2 = data[result2]
data2.to_excel('軟體銷售02.xlsx', index=False)
