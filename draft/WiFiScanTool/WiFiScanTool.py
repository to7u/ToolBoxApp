import subprocess
import datetime

class WiFiScanTool:
    def scan_wifi(self):
        with open("wifi_scan_result.txt", "a") as f:
            timestamp = datetime.datetime.now()
            f.write("Program executed at: " + str(timestamp) + "\n")

        # nmcliコマンドを実行してWiFiネットワークをスキャンする
        output = subprocess.check_output(['nmcli', 'device', 'wifi', 'list'])

        # スキャン結果をリストに変換する
        lines = output.decode().split('\n')
        networks = []
        for line in lines[1:-1]:
            columns = line.split()
            networks.append({'SSID': columns[0], 'BSSID': columns[1], 'CHAN': columns[2], 'FREQ': columns[3],'RATE': columns[4] + columns[5], 'SIGNAL': columns[6],'BARS': columns[7] , 'SECURITY': columns[8]})
            result = f"SSID: {columns[0]}, BSSID: {columns[1]}, CHAN: {columns[2]}, FREQ: {columns[3]},RATE: {columns[4]} + {columns[5]}, SIGNAL: {columns[6]},BARS: {columns[7]}, SECURITY: {columns[8]}\n"
            with open('wifi_scan_result.txt', 'a') as f:
                f.write(result)

        # スキャン結果を表示する
        for network in networks:
            print(network)

if __name__ == '__main__':
    wifi_scan_tool = WiFiScanTool()
    wifi_scan_tool.scan_wifi()