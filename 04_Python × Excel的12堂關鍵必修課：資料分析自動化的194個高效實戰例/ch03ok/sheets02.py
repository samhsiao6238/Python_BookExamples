import pandas as pd
data = pd.read_excel('工作表名稱.xlsx', sheet_name=None)
name = list(data.keys())
for i in name:
    print(i)
