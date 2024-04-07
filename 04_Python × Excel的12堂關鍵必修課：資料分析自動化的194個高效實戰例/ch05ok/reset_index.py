import pandas as pd
df=pd.read_excel("index1.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

df1=df.set_index("學校名稱")
print(df1)  
print()
df1=df.reset_index()
print(df1)  
print()
