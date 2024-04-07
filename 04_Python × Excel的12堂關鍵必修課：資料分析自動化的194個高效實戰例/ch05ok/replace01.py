import pandas as pd
df = pd.read_excel('書籍資訊.xlsx', sheet_name=0)
df = df.replace('網路行銷', '網際網路行銷')
df.to_excel('書籍資訊ok.xlsx', sheet_name='取代後', index=False)
