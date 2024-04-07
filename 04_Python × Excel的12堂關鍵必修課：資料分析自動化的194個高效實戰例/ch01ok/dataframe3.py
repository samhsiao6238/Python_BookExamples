import pandas as pd

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 180)  # 設置寬度

eng = ["apple", "banana", "mango", "watermelon"]
chi = ["蘋果", "香蕉", "芒果", "西瓜"]

dict = {"英文": eng, "中文": chi}
df = pd.DataFrame(dict, index=["單字1", "單字2", "單字3", "單字4"])
print(df)
