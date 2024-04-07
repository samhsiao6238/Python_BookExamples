import pandas as pd
df=pd.read_excel("book.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df.drop_duplicates())
print()
print(df.drop_duplicates(subset="書名"))
print()
print(df.drop_duplicates(subset=["書名","作者"]))
print()
print(df.drop_duplicates(subset=["書名","作者"],keep="last"))
