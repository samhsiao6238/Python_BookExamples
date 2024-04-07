import pandas as pd

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.width", 180)  # 設置寬度

df = pd.DataFrame(["apple", "banana", "mango", "watermelon"])
print(df)
print()
df = pd.DataFrame(
    [("apple", "蘋果"), ("banana", "香蕉"), ("mango", "芒果"), ("watermelon", "西瓜")]
)
print(df)
print()
df = pd.DataFrame(
    [["apple", "蘋果"], ["banana", "香蕉"], ["mango", "芒果"], ["watermelon", "西瓜"]]
)
print(df)
print()
