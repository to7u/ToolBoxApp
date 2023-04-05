import csv
import subprocess
import requests
import json

class ProxyScanTool:
    def __init__(self, ip_port_list_file, result_file):
        #self.ip_port_list_file = ip_port_list_file
        #self.result_file = result_file
        self.ip_port_list_file = "./poxy_list.csv"
        self.result_file = './proxy_scan_result.txt'
PingProxy
    # 対象ipから情報を入手するmethod
    def get_info(self,ip,port):
        req_url = "http://ipinfo.io/" + ip
        response = requests.get(req_url)
        country = response.json().get('country', '')
        region = response.json().get('region', '')
        #result = []
        #result.append([ip, port, country, region])
        return ip,port,country,region

    def scan_proxy(self):
        # CSVファイルからIPアドレスとポート番号を読み込む
        with open(self.ip_port_list_file, newline='') as f:
            reader = csv.reader(f)
            # ヘッダー行を読み飛ばす
            header = next(reader)
            ip_port_list = list(reader)

        # 結果を書き込むファイルを開く
        with open(self.result_file, 'w') as f:
            for row in ip_port_list:
                ip = row[0]
                port = row[1]

                # Pingを実行し、戻り値を取得
                result = subprocess.call(["ping", "-c", "1", "-w", "2", "-p", port, ip], stdout=subprocess.PIPE)

                # Pingの戻り値によってメッセージを出力
                if result == 0:
                    result = self.get_info(ip, port)
                    message = result[0] + ":" + result[1] + " is up!\n"
                    log = result[0] + ":" + result[1] + ":" + result[2] + ":" + result[3] + "\n"
                    f.write(log)
                    print(message)
                    print(result)
                else:
                    message = ip + ":" + port + " is down!\n"
                    #f.write(message)
                    #print(message)

if __name__ == "__main__":
    # PingCheckerのインスタンスを作成して、checkメソッドを実行する
    #checker = PingChecker('ip_port_list.csv', 'ping_result.txt')
    #checker.proxy_scan()

    proxt_scan_tool = ProxyScanTool()
    proxt_scan_tool.proxy_scan()
