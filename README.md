# Python Code Judger (比較兩個檔案執行的結果的程式)
這是一個基於 Python 開發的自動化評測腳本，可以自動讀取測試資料，並比對程式的螢幕輸出或產生的檔案內容是否符合預期。

## 套件列表
本專案僅使用 Python 內建的標準函式庫 (Standard Library)，環境中無須透過 pip 安裝任何外部套件即可順利執行。

主要使用的內建模組包含：
- `subprocess`：用於自動化執行受測的 Python 腳本，並擷取其在終端機 (stdout) 的輸出結果。
- `os`：用於路徑檢查與讀取自動產生的文字檔 (`read.txt` / `write.txt`)，以進行後續的內容比對。

## 成果展示

[🎬 點我觀看：作業執行展示影片](https://drive.google.com/file/d/1u-o5UEZ_Qz0W4EtmG9v5qDDg2rI8Xji/view?usp=sharing)

## 其它補充說明
本次測試包含 3 個題目：
1. 第 101 題：比對終端機輸出格式。
2. 第 301 題：比對終端機數字計算結果。
3. 第 902 題：讀取 `read.txt` 檔案內的數字並進行加總。
在處理檔案讀寫與資料切割時，使用了 `split()` 的預設無參數用法，成功過濾掉測試檔案中不規則的空白與換行符號。
<img width="396" height="532" alt="比對結果" src="https://github.com/user-attachments/assets/bf03e974-5358-42cf-b055-943854fce35b" />
