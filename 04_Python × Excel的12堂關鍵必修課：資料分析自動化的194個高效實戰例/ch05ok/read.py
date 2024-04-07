import pandas as pd
df=pd.read_excel("exam.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print(df)
print()
print("資料庫前五列學生欄位的內容:")
print(df['學生'][0:5])
print()
print("資料庫前三列學生欄位及校內檢測的內容:")
print(df[['學生','校內檢測']][0:3])
print()
