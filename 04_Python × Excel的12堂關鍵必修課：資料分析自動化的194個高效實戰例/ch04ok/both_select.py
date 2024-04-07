import pandas as pd
df=pd.read_excel("trip.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df) #原始資料庫
print()
print(df.loc[[0,2],["員工編號","第一喜好"]]) 
print()
print(df.iloc[[0,2],[0,2]]) 
print()
print(df.iloc[0:2,0:3]) 
print()
print(df[df["員工編號"]=="A0001"][["員工編號","第一喜好"]]) 
print()
