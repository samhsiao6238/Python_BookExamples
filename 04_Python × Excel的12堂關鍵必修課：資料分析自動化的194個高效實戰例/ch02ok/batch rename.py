from pathlib import Path
location = Path('border1')
file_list = location.glob('border*.xlsx')
for i in file_list:
    old = i.name
    new_name = old.replace('border', '邊框')
    new_path = i.with_name(new_name)
    i.rename(new_path)
