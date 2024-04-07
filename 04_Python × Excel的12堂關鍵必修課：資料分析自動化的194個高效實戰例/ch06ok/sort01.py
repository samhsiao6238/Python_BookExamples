import pandas as pd
data = pd.read_excel('教育訓練排序.xlsx', sheet_name='Sheet1')
data = data.sort_values(by='平均成績', ascending=False)
data.to_excel('教育訓練排序1.xlsx', sheet_name='Sheet1', index=False)
