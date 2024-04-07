import pandas as pd
data = pd.read_excel('銷售表.xlsx', sheet_name='總表')
pro_data = data[data['產品名稱'] == '離合器']
num_data = data[data['銷售數量'] >= 100]
pro_data.to_excel('離合器.xlsx', sheet_name='離合器', index=False)
num_data.to_excel('銷售數量大於等於100的記錄.xlsx', sheet_name='銷售數量大於等於100的記錄', index=False)
