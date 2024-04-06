# 載入必要套件
import os
import yfinance as yf
import pandas as pd


# yahoo 取用資料函數


def getDataFM(prod):
    # 備份文件的資料夾
    folder_name = "data"
    # 檢查資料夾是否存在
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 1. 定義備份檔案名稱
    bakfile = os.path.join(folder_name, f"{prod}.csv")
    # 2. 檢視是否有歷史資料(本地端)
    if os.path.exists(bakfile):
        yfdata = pd.read_csv(bakfile)
        yfdata["Date"] = pd.to_datetime(yfdata["Date"], format="%Y-%m-%d")
        yfdata.set_index("Date", inplace=True)
    else:
        yfdata = yf.download(f"{prod}.TW", period="max", progress=False)
        if yfdata.shape[0] == 0:
            yfdata = yf.download(f"{prod}.TWO", period="max", progress=False)
        yfdata.columns = [i.lower() for i in yfdata.columns]
        # 上網下載後 存到本地端
        yfdata.to_csv(bakfile)
    return yfdata


# yahoo 取用資料函數
def getDataYF(prod):
    # 備份文件的資料夾
    folder_name = "data"
    # 檢查資料夾是否存在
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 1. 定義備份檔案名稱
    bakfile = os.path.join(folder_name, f"yf_{prod}.csv")
    # 2. 檢視是否有歷史資料(本地端)
    if os.path.exists(bakfile):
        yfdata = pd.read_csv(bakfile)
        yfdata["Date"] = pd.to_datetime(yfdata["Date"], format="%Y-%m-%d")
        yfdata.set_index("Date", inplace=True)
    else:
        yfdata = yf.download(prod, period="max")
        yfdata.columns = [i.lower() for i in yfdata.columns]
        # 上網下載後 存到本地端
        yfdata.to_csv(bakfile)
    return yfdata


# 取得多商品歷史報酬率
def getMultipleReturn(getDataFunction, symbols, price_column):
    # 透過迴圈將不同商品報酬率計算出來
    datas = []
    for symbol in symbols:
        data = getDataFunction(symbol)
        # 分別計算報酬率
        returns = data[price_column].pct_change()
        cap_ret = 1 + returns
        cap_ret.name = symbol
        datas.append(cap_ret)
    # 將多商品報酬率整合
    all_ret = pd.concat(datas, axis=1)

    return all_ret
