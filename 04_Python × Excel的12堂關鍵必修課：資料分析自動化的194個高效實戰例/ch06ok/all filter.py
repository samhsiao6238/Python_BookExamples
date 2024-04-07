import pandas as pd
source = pd.read_excel('軟體銷售(按月份).xlsx', sheet_name=None)
with pd.ExcelWriter('業務人員A0901.xlsx') as workbook:
    for i in source:
        data = source[i]
        output = data[data['業務人員編號'] == 'A0901']
        output.to_excel(workbook, sheet_name=i, index=False)
