import pandas as pd
df=pd.read_excel("exam.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print(df)
print()
print("資料庫前五列內容:")
print(df.head())
print()
print("資料庫後三列內容:")
print(df.tail(3))
print()
