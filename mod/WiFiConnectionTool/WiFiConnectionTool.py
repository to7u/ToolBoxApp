import subprocess

class WiFiConnectionTool:
    # DEBUG
    def connection_cmd(self, ssid, iface):
        cmd = f"nmcli device wifi connect {ssid} iface {iface}"
        #subprocess.rum(cmd,shell=True)
        print(cmd)
    def connection_pass_cmd(self, ssid, password, iface):
        cmd = f"nmcli device wifi connect {ssid} password {password} iface {iface}"
        #subprocess.rum(cmd,shell=True)
        print(cmd)

    def run(self):
        menu_msg = '''
[WiFi Connextion Tool Menu]
[1] : WiFi connection
[2] : WiFi password connection 

[q] : quit
'''
        print(menu_msg)
        while True:
            answer = input('Please select a menu : ')
            if answer =='1':
                try:
                    ssid = input('Enter SSID : ')
                    iface = input('Enter interface name : ')
                    self.connection_cmd(ssid, iface)
                    break
                except:
                    print("command execution failed")
                    break
            elif answer =='2':
                try:
                    ssid = input('Enter SSID : ')
                    password = input('Enter password : ')
                    iface = input('Enter interface name : ')
                    self.connection_pass_cmd(ssid, password, iface)
                    break
                except:
                    print("command execution failed")
                    break
            elif answer == 'q':
                break

if __name__ == "__main__":
    wifi_connection_tool = WiFiConnectionTool()
    wifi_connection_tool.run()