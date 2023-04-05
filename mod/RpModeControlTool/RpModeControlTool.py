import subprocess
import configparser

'''
RaspberryPi用
Modeを切り替えるスクリプト

単体稼働を想定としている
moduleとして呼び出す際にはpathに関して改修が必要になる
'''

class RpModeControlTool:
    cmd_ap_open = "sh ./script/ApOpen.sh"
    cmd_ap_close = "sh ./script/ApClose.sh"
    cmd_createap_start = "sh ./script/CreateApStart.sh"
    cmd_createap_stop = "sh ./script/CreateApStop.sh"
    cmd_ufw_disable = "sh ./script/UfwDisable.sh"
    cmd_ufw_enable = "sh ./script/UfwEnable.sh"
    cmd_macchange_random_wlan0 = "sh ./script/MacchangeRandom_wlan0.sh"
    cmd_macchange_random_wlan1 = "sh ./script/MacchangeRandom_wlan1.sh"
    cmd_macchange_return_wlan0 = "sh ./script/MacchangeReturn_wlan0.sh"
    cmd_macchange_return_wlan1 = "sh ./script/MacchangeReturn_wlan1.sh"

    menu_msg = '''
[Mode Change Menu]

[1] : Private mode
[2] : Public mode
[3] : Open mode

[h] : help (show mode detail)
[q] : quit
'''
    help_msg = '''
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

    def private_mode(self):
        subprocess.run(cmd_ap_close,shell=True)
        subprocess.run(cmd_ufw_disable,shell=True)
        subprocess.run(cmd_macchange_return_wlan0,shell=True)
        subprocess.run(cmd_macchange_return_wlan1,shell=True)
    def public_mode(self):
        subprocess.run(cmd_ap_close,shell=True)
        subprocess.run(cmd_ufw_enable,shell=True)
        subprocess.run(cmd_macchange_random_wlan0,shell=True)
        #subprocess.run(cmd,shell=True)
    def open_mode(self):
        subprocess.run(cmd_ap_open,shell=True)
        subprocess.run(cmd_ufw_enable,shell=True)
        subprocess.run(cmd_macchange_random_wlan0,shell=True)
        subprocess.run(cmd_macchange_return_wlan1,shell=True)

# TODO 現在のmodeを保持/参照できるようにする
    #def logging_status(self):
    #def show_status(self):


    def run(self):
        print(self.menu_msg)
        while True:
            answer = input("Please select a menu : ")
            if answer == '1':
                # [1] : Private mode
                try:
                    print("private_mode")
                    private_mode()
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '2':
                # [2] : Public mode
                try:
                    print("public_mode")
                    public_mode()
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '3':
                # [3] : Open mode
                try:
                    print("open_mode")
                    open_mode()
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
    RpModeControlTool = RpModeControlTool()
    RpModeControlTool.run()
