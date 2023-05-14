import subprocess

class NordVpnTool:
    def show_Country(self):
        cmd = "nordvpn countries"
        print(cmd)

    def vpn_status(self):
        cmd = "nordvpn status"
        print(cmd)

    def vpn_connect(self):
        country = input("Please enter your country : ")
        cmd = f"nordvpn c {country}"
        print(cmd)
    
    def vpn_disconnect(self):
        cmd = "nordvpn d"
        print(cmd)
    
    def vpn_connect_double(self):
        country = input("Please enter your country : ")
        cmd = f"nordvpn connect --group double_vpn {country}"
        print(cmd)
    
    def run(self):
        menu_msg = '''/
[Nord VPN Tool Menu]

[1] : Show country
[2] : Show VPN status
[3] : Connect to VPN
[4] : Connect to Dubule VPN
[5] : Connect to VPN

[q] : quit
'''
        print(menu_msg)
        while True:
            answer = input('Please select a menu : ')
            if answer == '1':
                self.show_Country()
                #break
            elif answer == '2':
                self.vpn_status()
                #break
            elif answer == '3':
                self.vpn_connect()
                self.vpn_status()
                break
            elif answer == '4':
                self.vpn_connect_double()
                self.vpn_status()
                break
            elif answer == '5':
                self.vpn_disconnect()
                self.vpn_status()
                break
            elif answer == 'q':
                break
            else:
                print("Please enter agein.")
        print("Processing is complete.")

if __name__ == "__main__":
    nord_vpn_tool = NordVpnTool()
    nord_vpn_tool.run()