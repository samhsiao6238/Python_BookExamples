import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

left=pd.DataFrame({'id': ['A001', 'A002', 'A003', 'A004','A002', 'A003'],
                     '姓名': ['吳燦銘', '鄭苑鳳', '許伯如', '胡建文', '鄭苑鳳', '許伯如'],
                     '必修': ['數學', '程式語言', '網路行銷', '企業導論','影像繪圖', '公共關係']})
right=pd.DataFrame({'id': ['A001', 'A002', 'A003', 'A002', 'A003', 'A004'],
                   '選修': ['音樂', '日語', '泰語', '網球', '日語', '泰語'],})
rs = pd.merge(left, right, on='id')
print(left)
print("="*40)
print(right)
print("="*40)
print(rs)
