# -*- coding: utf-8 -*-
import mod_lite

# import するファイル名を記述(拡張子はいらない)
# import output
# output_text_class = output.output_class() # ファイル名.クラス名→インスタンス生成

'''

Linuxのみでの使用を想定しToolBoxAppより必要な機能のみを抽出したバージョン

'''

class MainControl:
    menu_msg = """
=== ToolBoxAppLITE Select menu ===

[Download tools]
[1] : WgetTool

[Configuration tools]
[2] : FireWallTool
[3] : TorConfigTool

[Convenient tools]
[4] : WiFiAnalyzerTool

[Others]
[h] : help
[q] : quit

==============================
"""
    help_msg = """
=== ToolBoxAppLITE Select menu ===
[Download tools]
[1] : WgetTool
対象URLを指定しサイト全体または、1階層のみを取得する

[Configuration tools]
[2] : FireWallTool
ファイアーウォールのON/OFF,設定投入を行う
(対応OS : Linux,Mac)

[3] : TorConfigTool
作成済み設定ファイルを読み込み、Tor Browserの接続ノード設定を変更する

[Convenient tools]
[7] : WiFiAnalyzerTool
周辺のWiFiをスキャンしリアルタイムに詳細を表示する

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
                # [1] : WgetTool
                wget_tool = mod_lite.WgetTool()
                print('Selected tool : ' + wget_tool.__class__.__name__)
                # DEBUG
                print("OK")
                #wget_tool.run()
                print('Processing completed : ' + wget_tool.__class__.__name__)
                continue
            elif select_num == '2':
                # [2] : FireWallTool
                firewall_tool = mod_lite.FirewallTool()
                print('Selected tool : ' + firewall_tool.__class__.__name__)
                firewall_tool.run()
                print('Processing completed : ' + firewall_tool.__class__.__name__)
                continue
            elif select_num == '3':
            	# [3] : TorConfigTool
                tor_config_tool = mod_lite.TorConfigTool()
                print('Selected tool : ' + tor_config_tool.__class__.__name__)
                tor_config_tool.run()
                print('Processing completed : ' + tor_config_tool.__class__.__name__)
                continue
            elif select_num == '4':
                # [4] : WiFiAnalyzerTool
                wifi_analyzer_tool = mod_lite.WiFiAnalayzerTool()
                print('Selected tool : ' + wifi_analyzer_tool.__class__.__name__)
                wifi_analyzer_tool.run()
                print('Processing completed : ' + wifi_analyzer_tool.__class__.__name__)
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