import subprocess

# WiFi用インターフェース設定用スクリプト

class WiFiConectionChangeTool:
    def run(self):
        interface = input("target interface :")
        ssid = input("SSID :")
        key = input("key :")
        cmd = f"sudo iwconfig {interface} essid {ssid} key s:{key}"

        try:
            print(cmd)
            subprocess.run(cmd, shell=True)
        except:
            print("error")

if __name__ == "__main__":
    wifi_conection_cheange_tool = WiFiConectionChangeTool()
    wifi_conection_cheange_tool.run()