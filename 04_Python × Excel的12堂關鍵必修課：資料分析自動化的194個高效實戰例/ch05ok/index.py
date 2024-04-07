import pandas as pd
df=pd.read_excel("index.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df)  #原資料內容
print()
df.index=[1,2,3,4,5,6,7,8,9]
print(df)  #新增列索引
print()
df.columns=["學校名稱","人數","季別"]
print(df)  #新增欄索引
print()
