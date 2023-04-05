import subprocess

# WiFi用インターフェース設定用スクリプト
interface = input("target interface :")
ssid = input("SSID :")
key = input("key :")
#cmd = f"sudo iwconfig {interface} essid {ssid} key s:{key}"
# 以下コマンドにて正常動作を確認
cmd = f"sudo nmcli device wifi connect {ssid} password {key}"

try:
    print(cmd)
    # subprocess.run(cmd, shell=True)
except:
    print("error")
