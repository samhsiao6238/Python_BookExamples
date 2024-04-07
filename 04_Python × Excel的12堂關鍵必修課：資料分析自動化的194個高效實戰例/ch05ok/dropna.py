import pandas as pd
df=pd.read_excel("isnull.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print("直接由print函數就可以查看缺失值:")
print(df)
print()
print("利用dropna函數刪除缺失值的所在列:")
print(df.dropna())
print()
