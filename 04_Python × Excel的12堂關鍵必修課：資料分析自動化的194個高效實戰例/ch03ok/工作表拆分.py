import pandas as pd
file_path = '軟體品項.xlsx'
data = pd.read_excel(file_path, sheet_name='銷售')
item = data.groupby('名稱')
for i, j in item:
    new_file_path = '拆分\\' + i + '.xlsx'
    j.to_excel(new_file_path, sheet_name=i, index=False)
