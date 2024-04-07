import pandas as pd
data = pd.read_excel('書籍訂單.xlsx', sheet_name=0)
top = data['總金額'].max()
interval = [0, 25000, 50002, top]
conclusion = ['不佳', '普通', '暢銷']
data['銷售情況'] = pd.cut(data['總金額'], interval, labels=conclusion)
data.to_excel('書籍訂單(評語).xlsx', sheet_name='銷售評估表', index=False)
