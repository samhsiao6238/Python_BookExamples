import pandas as pd
file_path = '軟體品項.xlsx'
data = pd.read_excel(file_path, sheet_name='銷售')
pro_data = data.groupby('名稱')
with pd.ExcelWriter('軟體品項拆分ok.xlsx') as wb:
    for i, j in pro_data:
        j.to_excel(wb, sheet_name=i, index=False)
