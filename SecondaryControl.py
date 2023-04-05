# -*- coding: utf-8 -*-

# import するファイル名を記述(拡張子はいらない)
# import output
# output_text_class = output.output_class() # ファイル名.クラス名→インスタンス生成

import mod

class MainControl:
    menu_msg = """
=== ToolBoxApp Select menu ===

[Download tools]
[1] : WebScrapingTool
[2] : WgetTool

[Convenient tools]
[3] : WiFiAnalyzerTool
[4] : FileEditTool

[Others]
[h] : help
[q] : quit

==============================
"""
    help_msg = """
=== ToolBoxApp Select menu ===
[Download tools]
[1] : WebScrapingTool
対象URLを指定し画像ファイルをすべて取得する

[2] : WgetTool
対象URLを指定しサイト全体または、1階層のみを取得する

[Convenient tools]
[3] : WiFiAnalyzerTool
周辺のWiFiをスキャンしリアルタイムに詳細を表示する

[4] : FileEditTool
・rename tool
srcディレクトリに存在するァイルの名称を"指定のもの + 連番"に変更しdstディレクトリへコピーする
・rename_random_auto tool
srcディレクトリに存在するァイルの名称をランダムなもの変更しdstディレクトリへコピーする
・rename_random_select tool
指定したパスに存在するファイルの名称をランダムなもの変更する
・resize tool
画像ファイルのサイズを変更する
・file conversion tool
対象ファイルの文字コードを変更する

==============================
"""
    def run(self):
        print(self.menu_msg)
        while True:
            print('--- MainControl Menu ---')
            print("[m] : Redisplay menu")
            select_num = input('Please enter the menu number : ')
            # [q]を選択して終了するまでループさせる(breakを入れない)
            if select_num == '1':
                # [1] : WebScrapingTool
                # インスタンス = モジュール名.クラス名
                web_scraping_tool = mod.WebScrapingTool()
                print('Selected tool : ' + web_scraping_tool.__class__.__name__)
                web_scraping_tool.run()
                print('Processing completed : ' + web_scraping_tool.__class__.__name__)
                continue
            elif select_num == '2':
                # [2] : WgetTool
                wget_tool = mod.WgetTool()
                print('Selected tool : ' + wget_tool.__class__.__name__)
                wget_tool.run()
                print('Processing completed : ' + wget_tool.__class__.__name__)
                continue
            elif select_num == '3':
                # [3] : WiFiAnalyzerTool
                wifi_analyzer_tool = mod.WiFiAnalayzerTool()
                print('Selected tool : ' + wifi_analyzer_tool.__class__.__name__)
                wifi_analyzer_tool.run()
                print('Processing completed : ' + wifi_analyzer_tool.__class__.__name__)
                continue
            elif select_num == '4':
                # [4] : FileEditTool
                file_edit_tool = mod.FileEditTool()
                print('Selected tool : ' + file_edit_tool.__class__.__name__)
                file_edit_tool.run()
                print('Processing completed : ' + file_edit_tool.__class__.__name__)
                continue
            elif select_num == 'h':
                print(self.help_msg)
                continue
            elif select_num == 'm':
                print(self.menu_msg)
                continue
            elif select_num == 'q':
                print('Exited from processing.')
                break
        print('All processing is completed.')


if __name__ == "__main__":
    main_control = MainControl()
    main_control.run()
