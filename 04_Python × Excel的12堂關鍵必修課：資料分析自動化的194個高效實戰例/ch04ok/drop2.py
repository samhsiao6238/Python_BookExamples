import pandas as pd
df=pd.read_excel("training.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df.drop([0,1,2,3,4],axis=0))
print()
print(df.drop(index=[0,1,2,3,4]))
print()
