import pandas as pd
all_data = pd.read_excel('辦公室用品採購表.xlsx', sheet_name=None)
with pd.ExcelWriter('篩選表.xlsx') as workbook:
    for i in all_data:
        data = all_data[i]
        filter_data = data[data['採購物品'] == '辦公桌']
        filter_data.to_excel(workbook, sheet_name=i, index=False)
