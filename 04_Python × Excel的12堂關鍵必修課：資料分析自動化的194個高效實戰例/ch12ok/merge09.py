import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

left=pd.DataFrame({'學號': ['A001', 'A002', 'A003', 'A004'],
                     '姓名': ['吳燦銘', '鄭苑鳳', '許伯如', '胡建文'],
                     '必修': ['數學', '程式語言', '網路行銷', '企業導論']})
print(left)
print("="*40)
right=pd.DataFrame({'學號': ['A001', 'A002', 'A005', 'A006'],
                      '姓名': ['吳燦銘', '鄭苑鳳', '許伯如', '胡建文'],
                      '選修': ['日語', '遊戲企劃', '經濟', '越語']})
print(right)
print("="*40)
rs = pd.merge(left,right ,on="學號",how="inner")
print(rs)
print("="*40)
rs = pd.merge(left,right ,on="學號",how="inner",suffixes=["_左邊","_右邊"])
print(rs)
