from pathlib import Path
location = Path('書籍資訊.xlsx')
print("主檔名:"+location.stem)
print("副檔名:"+location.suffix)
print("檔案全名:"+location.name)
