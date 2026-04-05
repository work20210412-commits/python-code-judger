# Python Code Judger (比較兩個檔案執行的結果的程式)
這是一個基於 Python 開發的自動化評測程式，可以自動讀取測試資料，並比對程式的螢幕輸出或產生的檔案內容是否符合預期。

## 安裝套件
本專案僅使用 Python 內建的標準函式庫 (Standard Library)，環境中無須透過 pip 安裝任何外部套件即可順利執行。

主要使用的內建模組包含：
- `subprocess`：用於自動化執行受測的 Python 腳本，並擷取其在終端機 (stdout) 的輸出結果。
- `os`：用於路徑檢查與讀取自動產生的文字檔 (`read.txt` / `write.txt`)，以進行後續的內容比對。

## 執行環境

* **Python**: 3.12.10 (或填寫你實際的 Python 版本)
* **OS**: Windows 11

## 檔案結構


├── data/                  # 專案相關數據資料夾
├── tests/                 # 受測程式碼與測試資料
│   ├── p101_fail.py     # 101題 錯誤版
│   ├── p101_ok.py       # 101題 正確版
│   ├── p301_fail.py     # 301題 錯誤版
│   ├── p301_ok.py       # 301題 正確版
│   ├── p902_fail.py     # 902題 錯誤版
│   ├── p902_ok.py       # 902題 正確版
│   └── PYD902_read.txt  # 902題 專用原始測試檔
├── app.py                 # 主程式 (自動評測腳本)
└── read.txt               # 供評測腳本讀取用之測試檔

使用方式
1.確保所有待測的 .py 檔案已放入 tests/ 資料夾中。

2.開啟終端機 (Terminal)，切換至專案根目錄。

3.執行以下指令啟動評測：
      python app.py
4.程式將自動依序執行測試，並在畫面上印出 ✅ [PASS] 或 ❌ [FAIL] 以及實際輸出差異。

## 成果展示

[🎬 點我觀看：作業執行展示影片](https://drive.google.com/file/d/1u_-o5UEz_Qz0w4EtmG9v5qDDg2ri8xji/view?usp=drive_link)

## 其它補充說明
本次測試包含 3 個題目：
1. 第 101 題：比對終端機輸出格式。
2. 第 301 題：比對終端機數字計算結果。
3. 第 902 題：讀取 `read.txt` 檔案內的數字並進行加總。
在處理檔案讀寫與資料切割時，使用了 `split()` 的預設無參數用法，成功過濾掉測試檔案中不規則的空白與換行符號。
<img width="396" height="532" alt="比對結果" src="https://github.com/user-attachments/assets/bf03e974-5358-42cf-b055-943854fce35b" />
