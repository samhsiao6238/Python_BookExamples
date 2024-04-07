import pandas as pd
df=pd.read_excel("exam.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print("取得複試欄位的數值的出現次數:")
print(df["複試"].value_counts())
print("取得複試欄位的數值的出現次數, 並列出不同值出現的佔比:")
print(df["複試"].value_counts(normalize=True))
