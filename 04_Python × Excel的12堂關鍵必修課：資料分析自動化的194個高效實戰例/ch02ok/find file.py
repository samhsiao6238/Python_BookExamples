from pathlib import Path
location = input('請輸入要尋找的資料夾絕對路徑：')
wb = input('你要找的活頁簿檔案名稱是：')
location = Path(location)
files= location.rglob(wb)
for i in files:
    print(i)
