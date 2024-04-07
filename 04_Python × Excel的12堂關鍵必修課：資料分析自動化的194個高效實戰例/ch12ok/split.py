import pandas as pd
data = pd.read_excel('sales.xlsx', sheet_name='全部人員')
title = list(data.columns)
reserve_title = data[['員工編號', '姓名']]
with pd.ExcelWriter('sales1.xlsx') as workbook:
    for i in title[2:]:
        each_title = data[i]
        sheet_data = pd.concat([reserve_title, each_title], axis=1)
        sheet_data.to_excel(workbook, sheet_name=i, index=False)
