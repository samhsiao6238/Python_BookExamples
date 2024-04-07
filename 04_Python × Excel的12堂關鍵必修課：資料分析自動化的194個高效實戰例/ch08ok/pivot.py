import pandas as pd
df=pd.read_excel("pivot.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度
#原資料庫
print(df)
print("="*50)
print(pd.pivot_table(df,values="學號",columns="組別",index="班級",
                     aggfunc='count',margins=True))
print("="*50)
print(pd.pivot_table(df,values="學號",columns="組別",index="班級",
                     aggfunc='count',margins=True,
                     fill_value=0,margins_name="人數統計"))
