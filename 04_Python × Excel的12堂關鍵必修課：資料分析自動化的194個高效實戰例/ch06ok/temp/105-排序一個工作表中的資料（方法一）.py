import pandas as pd
data = pd.read_excel('銷售表.xlsx', sheet_name='總表')
data = data.sort_values(by='利潤', ascending=False)
data.to_excel('銷售表1.xlsx', sheet_name='總表', index=False)
