import pandas as pd
df=pd.read_excel("score.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

df["總分"]=df["初級"]+df["中級"]
df["平均"]=df["總分"]/2
print(df)
