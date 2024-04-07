import pandas as pd
df=pd.read_excel("summary02.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度
#原資料庫
df.index=["NO1","NO2", "NO3","NO4","NO5", "NO6","NO7"]
print("總和")
print(df.sum(axis=1))
print("平均值")
print(df.mean(axis=1))
print("中位數")
print(df.median())
