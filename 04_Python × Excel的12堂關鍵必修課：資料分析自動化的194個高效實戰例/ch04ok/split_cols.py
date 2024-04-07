import pandas as pd
ave_time = pd.read_excel('全馬平均時間.xlsx', sheet_name=0)
temp = ave_time['平均時間'].str.split('*', expand=True)
ave_time['時'] = temp[0]
ave_time['分'] = temp[1]
ave_time['秒'] = temp[2]
ave_time.drop(columns=['平均時間'], inplace=True)
ave_time.to_excel('全馬平均時間ok.xlsx', sheet_name='總表', index=False)
