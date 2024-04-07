from time import localtime
from pathlib import Path
location = Path('日期分類')
files = location.glob('*.xls*')
for i in files:
    lm_time = i.stat().st_mtime
    folder_name = localtime(lm_time).tm_year
    new_location = location / str(folder_name) 
    if not new_location.exists():
        new_location.mkdir(parents=True)
    i.replace(new_location / i.name)
