from pathlib import Path
old = Path('書籍清單.xlsx')
new = Path('書籍資訊.xlsx')
old.rename(new)
