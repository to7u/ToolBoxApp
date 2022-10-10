import subprocess

"""
各オプション補足
各オプション

-r 
回帰的クローリング

-l
階層指定
1 カレント
0 全階層

-p
画像ファイルも併せて取得

-k
ローカル参照用にファイルパスを絶対→相対に変換
メモ:これがapacheで参照できない原因？

-w N
ダウンロードごとにN秒待機する

--random-wait
-wで指定した数の0.5~1.5倍の時間待機する
"""

class WgetTool:
    # 全体
    wget_all_cmd = "wget -r -l 0 -w 5 --random-wait -p -k "
    # カレントのみ
    wget_single_cmd = "wget -r -l 1 -w 5 --random-wait -p "

    def run(self):
        menu_msg = """
=== select menu ===
[1] : wget all page : 
[2] : wget single page : 

[q] : exit process
===================
"""
        print(menu_msg)

        while True:
            menu_num = input("select menu number : ")
            if menu_num == "1":
                target_url = input("Please enter the target URL : ")
                try:
                    print("Processing started")
                    subprocess.run(self.wget_all_cmd + target_url,shell=True)
                    print(self.wget_all_cmd + target_url)
                except:
                    print("ERROR : Processing did not complete normally")
                break
            elif menu_num == "2":
                target_url = input("Please enter the target URL : ")
                try:
                    print("Processing started")
                    subprocess.run(self.wget_single_cmd + target_url,shell=True)
                    print(self.wget_single_cmd + target_url)
                except:
                    print("ERROR : Processing did not complete normally")
                break
            elif menu_num == 'q':
                print('exit process')
                break
            else:
                print("Please enter agein.")
        print("Processing is complete.")

if __name__ == "__main__":
    wget_tool = WgetTool()
    wget_tool.run()