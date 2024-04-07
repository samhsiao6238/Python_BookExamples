import pandas as pd
df=pd.read_excel("group.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度
#原資料庫
print(df)
print(df.groupby(["班級","組別"]).aggregate(["count","sum"]))
print(df.groupby(["班級","組別"]).aggregate({"學號":"count","第一次":"sum","第二次":"sum","第三次":"sum"}))
