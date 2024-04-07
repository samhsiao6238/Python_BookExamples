import pandas as pd
df=pd.read_excel("training.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

print(df)
print("電腦應用共有下列幾種分數: ")
print(df["電腦應用"].unique())
print()
