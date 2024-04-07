from pathlib import Path
location = Path('副檔名分類')
files = location.glob('*.xls*')
for i in files:
    extension = i.suffix
    new_location = location / extension
    if not new_location.exists():
        new_location.mkdir()
    i.replace(new_location / i.name)
