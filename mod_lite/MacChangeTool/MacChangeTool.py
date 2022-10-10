import subprocess

# MACアドレス変更用スクリプト
# macchangerツールをsubprocessで呼び出して実行する
'''
■ MacChanger 使い方

●現在状態の確認
$ macchanger -s {対象インターフェース}

●ランダムな MAC アドレスに設定
$ ifconfig {対象インターフェース} down
$ macchanger -r {対象インターフェース}
$ ifconfig {対象インターフェース} up

●元に戻す
$ ifconfig {対象インターフェース} down
$ macchanger -p {対象インターフェース}
$ ifconfig {対象インターフェース} up

●指定の MAC アドレスに設定
$ ifconfig {対象インターフェース} down
$ macchanger -m 00:11:22:33:44:55 {対象インターフェース}
'''

class MacChangeTool:
    def interface_down(self, interface):
        cmd = f"ifconfig {interface} down"
        subprocess.run(cmd, shell=True)

    def interface_up(self, interface):
        cmd = f"ifconfig {interface} up"
        subprocess.run(cmd, shell=True)

    def show_mac(self, interface):
        cmd = f"macchanger -s {interface}"
        subprocess.run(cmd, shell=True)

    def change_mac(self, interface, address):
        cmd = f"macchanger -m {address} {interface}"
        subprocess.run(cmd, shell=True)
    
    def change_mac_random(self, interface):
        cmd = f"macchanger -r {interface}"
        subprocess.run(cmd, shell=True)
    
    def change_default(self, interface):
        cmd = f"macchanger -p {interface}"
        subprocess.run(cmd, shell=True)
    
    def run(self):
        menu_msg = '''/
[Mac Change Tool Menu]

[1] : Show status
[2] : Change MAC address
[3] : Change random MAC address
[4] : Change default MAC address

[q] : quit
'''     
        print(menu_msg)
        while True:
            answer = input('Please select a menu : ')
            if answer == '1':
                # show_mac
                interface = input('Enter interface name : ')
                try:
                    self.show_mac(interface)
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '2':
                # change_mac
                interface = input('Enter interface name : ')
                address = input('Enter MAC address : ')
                try:
                    self.interface_down(interface)
                    self.change_mac(interface, address)
                    self.interface_up(interface)
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '3':
                # change_mac_random
                interface = input('Enter interface name : ')
                try:
                    self.interface_down(interface)
                    self.change_mac_random(interface)
                    self.interface_up(interface)
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == '4':
                # change_mac_default
                interface = input('Enter interface name : ')
                try:
                    self.interface_down(interface)
                    self.change_default(interface)
                    self.interface_up(interface)
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == 'q':
                break


if __name__ == "__main__":
    mac_change_tool = MacChangeTool()
    mac_change_tool.run()