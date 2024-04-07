import pandas as pd
df=pd.read_excel("trip.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df) #原始資料庫
print()
print(df.loc[0]) #單一列
print()
print(df.loc[[0,3,5]]) #多數列以串列表示
print()
print(df.iloc[0:5]) #選取連續多列
print()
print(df[df["員工編號"]=="A0001"]) #根據設定條件來篩選
print()
