import pandas as pd
df = pd.read_excel('外包人員.xlsx', sheet_name=None)
with pd.ExcelWriter('外包人員ok.xlsx') as wb:
    for i, j in df.items():
        df = j.replace('元益喜', '袁益喜')
        df.to_excel(wb, sheet_name=i, index=False)
