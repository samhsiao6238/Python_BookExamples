import pandas as pd
df=pd.read_excel("exam.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print(df)
print()
print("取得所有數值型別的分佈值情況:")
print(df.describe())
