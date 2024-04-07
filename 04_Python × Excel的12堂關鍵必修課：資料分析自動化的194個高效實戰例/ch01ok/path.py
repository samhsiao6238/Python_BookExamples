from pathlib import Path

# 檔案路徑
path = Path("myfile.txt")
print("建立檔案前是否有這個檔案? ", path.is_file())
# 建立檔案
path.touch()
# 檢查是否有這個檔案
print("建立檔案後是否有這個檔案? ", path.is_file())
# 在檔案中寫入文字
path.write_text("happy birthday")
# 讀取檔案的文字並輸出
print("目前檔案的文字: ", path.read_text())
# 在檔案中寫入文字會以覆寫的方式寫入檔案
path.write_text("I love holiday.")
# 讀取檔案的文字並輸出覆寫後的檔案內容
print("覆寫檔案的文字: ", path.read_text())

# 檔案的詳細資料
print("檔案的詳細資料: ", path.stat())
# 刪除檔案
print(path.unlink())
# 檢查檔案是否存在
print("檔案是否存在? ", path.exists())
