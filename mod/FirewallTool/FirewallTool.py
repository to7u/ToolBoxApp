import  subprocess
import platform

class FirewallTool:
    def get_os(self):
        pf = platform.system()
        #print(pf)
        if pf == 'Windows':
            print('on Windows')
        elif pf == 'Darwin':
            print('on Mac')
        elif pf == 'Linux':
            print('on Linux')
        return pf

    def linux_conf(self):
        show_cmd = 'systemctl is-active ufw'
        show_rule_cmd = 'ufw status verbose'
        show_rule_num_cmd = 'ufw status numbered'
        start_cmd = 'systemctl start ufw'
        stop_cmd = 'systemctl stop ufw'
        
        # log path : /var/log/ufw.log
        logging_on_cmd = 'ufw logging on'
        logging_off_cmd = 'ufw logging off'
        
        # ufw allow <port num>
        allow_tcp_port = 'ufw allow' + ' '
        # ufw allow <port num>/udp
        allow_udp_port = 'ufw allow' + ' '
        # ufw delete <numberd>
        delete_rule_cmd = 'ufw delete' + ' '
        reset_rule_cmd = 'ufw reset'
        
        menu_msg = '''/
[Linux os Firewall Tool Menu]

[1] : Firewall on
[2] : Firewall off
[3] : Logging on
[4] : Logging off
[5] : Add TCP rule
[6] : Add UDP rule
[7] : Delete rule
[8] : Reset rule

[q] : quit
'''
        print(menu_msg)
        subprocess.run(show_cmd,shell=True)
        subprocess.run(show_rule_cmd,shell=True)
        while True:
            answer = input('Please select a menu : ')
            if answer == '1':
                subprocess.run(start_cmd,shell=True)
                subprocess.run(show_cmd,shell=True)
                break
            elif answer == '2':
                subprocess.run(stop_cmd,shell=True)
                subprocess.run(show_cmd,shell=True)
                break
            elif answer == '3':
                subprocess.run(logging_on_cmd,shell=True)
                subprocess.run(show_rule_cmd,shell=True)
                break
            elif answer == '4':
                subprocess.run(logging_off_cmd,shell=True)
                subprocess.run(show_rule_cmd,shell=True)
                break
            elif answer == '5':
                subprocess.run(show_rule_cmd,shell=True)
                port_num = input('Please select  port number : ')
                subprocess.run(allow_tcp_port + port_num,shell=True)
                subprocess.run(show_rule_cmd,shell=True)
                break
            elif answer == '6':
                subprocess.run(show_rule_cmd,shell=True)
                port_num = input('Please select  port number : ')
                subprocess.run(allow_udp_port + port_num + ' /udp',shell=True)
                subprocess.run(show_rule_cmd,shell=True)
                break
            elif answer == '7':
                subprocess.run(show_rule_num_cmd,shell=True)
                rule_num = input('Please select  rule number : ')
                subprocess.run(delete_rule_cmd + rule_num,shell=True)
                subprocess.run(show_rule_num_cmd,shell=True)
                break
            elif answer == '8':
                subprocess.run(show_cmd,shell=True)
                subprocess.run(show_rule_cmd,shell=True)
                subprocess.run(reset_rule_cmd,shell=True)
                subprocess.run(show_cmd,shell=True)
                subprocess.run(show_rule_cmd,shell=True)
                break
            elif answer == 'q':
                break

    def mac_conf(self):
        # os ver によっては正常に稼働しない可能性あり
        start_cnd = 'sudo defaults write /Library/Preferences/com.apple.alf globalstate -int 1'
        stop_cmd = 'sudo defaults delete /Library/Preferences/com.apple.alf globalstate'
        menu_msg = '''/
[Mac os Firewall Tool Menu]

[1] : Firewall on
[2] : Firewall off

[99]: Exit the process
'''
        print(menu_msg)
        while True:
            answer = input('Please select a menu : ')
            if answer == '1':
                subprocess.run(start_cnd, shell=True)
                break
            elif answer == '2':
                subprocess.run(stop_cmd, shell=True)
                break
            elif answer == '99':
                break
    
    def run(self):
        platform = self.get_os()
        if platform == 'Windows':
            print('Processing for windows is not implemented.')
        elif platform == 'Darwin':
            self.mac_conf()
        elif platform == 'Linux':
            self.linux_conf()

if __name__ == "__main__":
    firewall_tool = FirewallTool()
    firewall_tool.run()