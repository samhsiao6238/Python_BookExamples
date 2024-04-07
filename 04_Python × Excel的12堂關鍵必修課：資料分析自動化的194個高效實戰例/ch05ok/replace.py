import pandas as pd
df=pd.read_excel("book1.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print()
print(df)  #原資料內容
print()
print(df.replace("C#語言", "C Sharp"))
print()
df["定價"].replace(620,600,inplace=True)
print(df)
print() #新資料內容
df["定價"].replace([480,500],520,inplace=True)
print(df)
print() #新資料內容
