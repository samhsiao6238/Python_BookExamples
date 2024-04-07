import pandas as pd
ave_time = pd.read_excel('全馬平均時間ok.xlsx', sheet_name='總表')
ave_time['平均時間'] = ave_time['時'].astype(str) + '*' \
+ ave_time['分'].astype(str) + '*' + ave_time['秒'].astype(str)
ave_time.drop(columns=['時', '分', '秒'], inplace=True)
ave_time.to_excel('全馬平均時間1.xlsx', sheet_name='Sheet1', index=False)
