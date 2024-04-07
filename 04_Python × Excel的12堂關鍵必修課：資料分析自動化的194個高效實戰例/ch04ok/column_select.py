import pandas as pd
df=pd.read_excel("trip.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df) #原始資料庫
print()
print(df["姓名"]) #單一欄位
print()
print(df[["員工編號","第一喜好"]]) #多數欄以串列表示
print()
print(df.iloc[:,[0,2]]) #另外一種位置索引法
print()
