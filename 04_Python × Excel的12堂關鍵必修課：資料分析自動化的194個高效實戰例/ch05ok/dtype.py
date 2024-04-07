import pandas as pd
df=pd.read_excel("exam.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print(df)
print()
print("取得學生欄位的資料類型:")
print(df["學生"].dtype)
print("取得學號欄位的資料類型:")
print(df["學號"].dtype)
print("取得校內檢測欄位的資料類型:")
print(df["校內檢測"].dtype)
