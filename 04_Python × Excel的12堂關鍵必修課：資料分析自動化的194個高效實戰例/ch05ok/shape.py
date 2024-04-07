import pandas as pd
df=pd.read_excel("exam.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

#資料庫內容
print(df)
print()
print("檢查檔案大小:")
print('會以一組括號來顯示這個檔案目前由多少列(rows)及多少行(columns)')
print(df.shape)
