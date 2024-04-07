import pandas as pd
data = pd.read_excel('軟體銷售.xlsx', sheet_name='銷售業績')
info1 = data[data['產品種類'] == '應用軟體']
info2 = data[data['總金額'] >= 30000000]
info1.to_excel('應用軟體軟體銷售.xlsx', sheet_name='應用軟體', index=False)
info2.to_excel('暢銷商品.xlsx', sheet_name='暢銷商品', index=False)
