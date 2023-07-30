# -*- coding: utf-8 -*-

# import するファイル名を記述(拡張子はいらない)
# import output
# output_text_class = output.output_class() # ファイル名.クラス名→インスタンス生成

import mod

class MainControl:
    menu_msg = """
=== ToolBoxApp Select menu ===

[Configuration tools]
[1] : FireWallTool
[2] : MacChengerTool
[3] : IpChengerTool
[4] : TorConfigTool

[Test : Draft tools]
[5] : ProxyScanTool
[6] : NwSanTool
[7] : WiFiScanTool
[8] : WiFiConnectionTool

[Others]
[h] : help
[q] : quit

==============================
"""
    help_msg = """
=== ToolBoxApp Select menu ===

[Configuration tools]
[1] : FireWallTool
ファイアーウォールのON/OFF,設定投入を行う
(対応OS : Linux,Mac)

[2] : MacChengerTool
対象インターフェースを指定しMACアドレスを変更する

[3] : IpChengerTool
対象インターフェースを指定しIPアドレスを変更する
固定/自動による設定が可能

[4] : TorConfigTool
作成済み設定ファイルを読み込み、Tor Browserの接続ノード設定を変更する

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
                # [1] : FireWallTool
                firewall_tool = mod.FirewallTool()
                print('Selected tool : ' + firewall_tool.__class__.__name__)
                firewall_tool.run()
                print('Processing completed : ' + firewall_tool.__class__.__name__)
                continue
            elif select_num == '2':
                # [2] : MacChengerTool
                mac_chenger_tool = mod.MacChangeTool()
                print('Selected tool : ' + mac_chenger_tool.__class__.__name__)
                mac_chenger_tool.run()
                print('Processing completed : ' + mac_chenger_tool.__class__.__name__)
                continue
            elif select_num == '3':
                # [3] : IpChengerTool
                ip_chenger_tool = mod.IpChangeTool()
                print('Selected tool : ' + ip_chenger_tool.__class__.__name__)
                ip_chenger_tool.run()
                print('Processing completed : ' + ip_chenger_tool.__class__.__name__)
                continue
            elif select_num == '4':
                # [4] : TorConfigTool
                tor_config_tool = mod.TorConfigTool()
                print('Selected tool : ' + tor_config_tool.__class__.__name__)
                tor_config_tool.run()
                print('Processing completed : ' + tor_config_tool.__class__.__name__)
                continue
            # Test Draft tools
            elif select_num == '5':
                proxy_scan_tool = mod.ProxyScanTool()
                print('Selected tool : ' + proxy_scan_tool.__class__.__name__)
                proxy_scan_tool.run()
                print('Processing completed : ' + proxy_scan_tool.__class__.__name__)
                continue
            elif select_num == '6':
                nw_scan_tool = mod.NwScanTool()
                print('Selected tool : ' + nw_scan_tool.__class__.__name__)
                nw_scan_tool.run()
                print('Processing completed : ' + nw_scan_tool.__class__.__name__)
                continue
            elif select_num == '7':
                wifi_scan_tool = mod.WiFiScanTool()
                print('Selected tool : ' + wifi_scan_tool.__class__.__name__)
                wifi_scan_tool.run()
                print('Processing completed : ' + wifi_scan_tool.__class__.__name__)
                continue
            elif select_num == '8':
                wifi_connection_tool = mod.WiFiConnectionTool()
                print('Selected tool : ' + wifi_connection_tool.__class__.__name__)
                wifi_connection_tool.run()
                print('Processing completed : ' + wifi_connection_tool.__class__.__name__)
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
