import pandas as pd
all_data = pd.read_excel('辦公室用品採購表.xlsx', sheet_name=None)
datas = pd.DataFrame()
for i in all_data:
    data = all_data[i]
    filter_data = data[data['採購物品'] == '辦公桌']
    datas = pd.concat([datas, filter_data], axis=0)
datas.to_excel('辦公桌.xlsx', sheet_name='辦公桌', index=False)
