import pandas as pd
df=pd.read_excel("isnull.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print("直接由print函數就可以查看缺失值:")
print(df)
print()
print("使用fillna函數將缺失值填入值:")
print(df.fillna(0))

print("利用fillna函數以字典方式填入值:")
df1=df.fillna({"定價":500,"數量":100})
print(df1)
df1.to_excel(excel_writer="fillna.xlsx")
