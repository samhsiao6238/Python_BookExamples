import pandas as pd
df=pd.read_excel("training.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print("電腦應用的分數區間的分佈情況: ")
print(pd.cut(df["電腦應用"],bins=[0,60,70,80,90,100]))
print()
print("電腦應用的分數分成 5 等份: ")
print(pd.qcut(df["電腦應用"],5))
print()
