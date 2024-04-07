from pathlib import Path
location = input('請輸入尋找要尋找的資料夾絕對路徑：')
keyword = input('要找的活頁簿檔名關鍵字：')
location = Path(location)
files = location.rglob(f'*{keyword}*.xls*')
for i in files:
    print(i)
