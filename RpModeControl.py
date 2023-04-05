import mod_lite
'''

RaspberryPi用
Modeを切り替えるスクリプト
mod_lite配下のモジュール使用

'''

# TODO 現在のmodeをフラグなどで保持して参照できるようにすると良いかもしれない

class ModeChange:
    # 各ツールのインスタンスを作成
    wifi_conection_change_tool = mod_lite.WiFiConectionChangeTool() # wlan0 接続先変更
    Wifi_mode_change_tool = mod_lite.WiFiModeChangeTool() # wlan1 WiFiモード変更
    firewall_tool = mod_lite.FirewallTool() # Firewall 設定変更
    macchange_tool = mod_lite.MacChangeTool() # Macaddress 設定変更

    menu_msg = '''/
[Mode Change Menu]

[1] : Private mode
[2] : Public mode
[3] : Open mode

[h] : help (show mode detail)
[q] : quit
'''
    help_msg = '''/
[Mode detail]

Private mode
WiFi : stealth
UFW  : off
MAC  : default(0,1)

Public mode
WiFi : stealth
UFW  : on
MAC  : wlan0

Open mode
WiFi : open
UFW  : on
MAC  : wlan0,1
'''

    def run(self):
        print(self.menu_msg)
        while True:
            answer = input('Please select a menu : ')
            if answer == '1':
                # [1] : Private mode
                try:
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '2':
                # [2] : Public mode
                try:
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '3':
                # [3] : Open mode
                try:
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == 'h':
                try:
                    print(self.help_msg)
                except:
                    print("command execution failed")
                    break
            elif answer == 'q':
                break


if __name__ == "__main__":
    mode_change = ModeChange()
    mode_change.run()
