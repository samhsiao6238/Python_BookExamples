import pandas as pd
df1=pd.read_excel("score1.xlsx")
df2=pd.read_excel("score2.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df1)
print("="*40)
print(df2)
print("="*40)
rs = pd.concat([df1,df2], join='outer')
print(rs)
