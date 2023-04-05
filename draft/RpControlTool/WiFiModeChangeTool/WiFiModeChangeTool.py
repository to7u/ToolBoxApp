import subprocess
import configparser
import os
import errno

# WiFi stealth / open 切り替えスクリプト
# TODO 単体テスト未実施

class WiFiModeChangeTool:
    # config.iniから設定を読み込むよう改修
    config_ini = configparser.ConfigParser()
    #config_ini_path = './config/config.ini'
    # 個人環境ini読み込み
    config_ini_path = './config/my_config.ini'
    # config.iniの有無を確認
    if not os.path.exists(config_ini_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)
    config_ini.read(config_ini_path, encoding='utf-8')

    config_path = config_ini['PATH']['config_path']
    stealth_config = config_ini['FILE']['stealth_config']
    open_config = config_ini['FILE']['open_config']
    active_config = config_ini['FILE']['active_config']

    def show_ap_status(self):
        cmd = f'cat {self.config_path + self.active_config}'
        try:
            subprocess.run(cmd, shell=True)
        except:
            print("command execution failed")

    def restart_ap(self):
        cmd = 'systemctl restart create_ap.service'
        try:
            subprocess.run(cmd, shell=True)
        except:
            print("command execution failed")

    def wifi_stealth(self):
        rm_cmd = f'rm -f {self.config_path + self.active_config}'
        set_cmd = f'cp {self.config_path + self.stealth_config} {self.active_config}'
        try:
            subprocess.run(rm_cmd, shell=True)
            subprocess.run(set_cmd, shell=True)
            self.restart_ap()
        except:
            print("command execution failed")
    
    def wifi_open(self):
        rm_cmd = f'rm -f {self.config_path + self.active_config}'
        set_cmd = f'cp {self.config_path + self.open_config} {self.active_config}'
        try:
            subprocess.run(rm_cmd, shell=True)
            subprocess.run(set_cmd, shell=True)
            self.restart_ap()
        except:
            print("command execution failed")
    
    def run(self):
        menu_msg = '''/
[WiFi Mode Change Menu]

[1] : Show status
[2] : Change WiFi mode : Stealth
[3] : Change WiFi mode : Open

[q] : quit
'''
        print(menu_msg)
        while True:
            answer = input('Please select a menu : ')
            if answer == '1':
                break
            elif answer == '2':
                break
            elif answer == '3':
                break
            elif answer == 'q':
                break


if __name__ == "__main__":
    wifi_mode_cheange_tool = WiFiModeChangeTool()
    wifi_mode_cheange_tool.run()