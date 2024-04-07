from pathlib import Path
location = Path('border')
files = location.glob('*.xls*')
for i in files:
    print(i.name)
