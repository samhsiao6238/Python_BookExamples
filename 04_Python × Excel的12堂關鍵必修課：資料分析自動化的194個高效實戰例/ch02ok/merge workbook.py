from pathlib import Path
import pandas as pd
folder_path = Path('合併業績表')
files = folder_path.glob('*.xls*')
with pd.ExcelWriter('合併活頁簿.xlsx') as wb:
    for i in files:
        stem_name = i.stem
        data = pd.read_excel(i, sheet_name=0)
        data.to_excel(wb, sheet_name=stem_name, index=False)
