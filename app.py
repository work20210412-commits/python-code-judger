import subprocess
import os

def check_result(title, script_path, input_str, expected_stdout=None, expected_file_data=None):
    print(f"--- 測試題目: {title} ({script_path}) ---")
    
    try:
        # 執行程式
        proc = subprocess.run(
            ['python', script_path],
            input=input_str,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=5
        )
        
        # 處理螢幕輸出：移除前後空白，並將換行符號統一
        actual_stdout = proc.stdout.strip().replace('\r\n', '\n')
        is_pass = True

        # 1. 檢查螢幕輸出 (101, 301, 902)
        if expected_stdout is not None:
            exp_stdout = expected_stdout.strip().replace('\r\n', '\n')
            # 逐行比對，避免行末空格干擾
            actual_lines = [line.rstrip() for line in actual_stdout.splitlines()]
            expected_lines = [line.rstrip() for line in exp_stdout.splitlines()]
            
            if actual_lines != expected_lines:
                is_pass = False
        
        # 2. 檢查產生的檔案 (901)
        if expected_file_data is not None:
            if os.path.exists("write.txt"):
                with open("write.txt", "r", encoding="utf-8") as f:
                    file_content = f.read().strip().replace('\r\n', '\n')
                    exp_file = expected_file_data.strip().replace('\r\n', '\n')
                    if file_content != exp_file:
                        is_pass = False
            else:
                is_pass = False

        if is_pass:
            print("結果: ✅ [PASS]")
        else:
            print("結果: ❌ [FAIL]")
            print(f"[實際輸出]:\n{actual_stdout}")
            if expected_file_data and not is_pass:
                print("註：檔案內容比對不吻合")

    except Exception as e:
        print(f"執行出錯: {e}")
    print("-" * 30 + "\n")

if __name__ == "__main__":
    # --- 101 題修正 ---
    in_101 = "85\n4\n299\n478\n"
    ans_101 = (
        "|   85     4|\n"
        "|  299   478|\n"
        "|85    4    |\n"
        "|299   478  |"
    )
    check_result("101 正確", "tests/p101_ok.py", in_101, expected_stdout=ans_101)
    check_result("101 錯誤", "tests/p101_fail.py", in_101, expected_stdout=ans_101)

    # --- 301 題 ---
    in_301 = "66\n666\n"
    ans_301 = "219966"
    check_result("301 正確", "tests/p301_ok.py", in_301, expected_stdout=ans_301)
    check_result("301 錯誤", "tests/p301_fail.py", in_301, expected_stdout=ans_301)

    # --- 902 題 (資料加總) ---
    # 做法：902題需要讀取 read.txt，所以我們要在測試前先寫入測試資料
    test_data_902 = "11 22 33 22 33 44 33 44 55 44 55 66 55 66 77"
    with open("read.txt", "w", encoding="utf-8") as f:
        f.write(test_data_902)
    
    # 902 題沒有從鍵盤輸入 (input_str 為空字串)，結果直接印在螢幕上
    ans_902 = "660"
    check_result("902 正確", "tests/p902_ok.py", input_str="", expected_stdout=ans_902)
    check_result("902 錯誤", "tests/p902_fail.py", input_str="", expected_stdout=ans_902)