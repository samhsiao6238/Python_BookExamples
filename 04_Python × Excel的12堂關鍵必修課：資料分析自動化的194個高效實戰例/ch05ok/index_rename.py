import pandas as pd
df=pd.read_excel("index1.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

df.index=[1,2,3,4,5,6,7,8,9,10]
print(df)  #新增列索引
print()
print(df.rename(columns={"學校名稱":"校名","季別":"班別"},
                index={1:"A",2:"B",3:"C",4:"D",5:"E",
                       6:"F",7:"G",8:"H",9:"I",10:"J"}))
print()
