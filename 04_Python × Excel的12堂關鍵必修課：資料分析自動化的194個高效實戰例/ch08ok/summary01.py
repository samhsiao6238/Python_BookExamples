import pandas as pd
df=pd.read_excel("summary01.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度
#原資料庫
print(df)
print("預設的情況會計算每行的非NA 儲存格個數")
print(df.count())
print("設定axis=1, 計算每的列非NA 儲存格個數")
print(df.count(axis=1))
print("#直接指定欄位來檢查該行的非NA 儲存格個數")
print("欄位名稱: 第一喜好")
print(df["第一喜好"].count())
