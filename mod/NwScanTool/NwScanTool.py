# pip install python-nmap
import nmap

class NwScanTool:
    def __init__(self):
        #target_network = input("Enter address : ")  # スキャンするネットワークの範囲を指定
        self.target_file = './log/nw_scan_results.txt'  # 結果を保存するファイル名を指定

    def scan_network(self):
        target_network = input("Enter address : ")  # スキャンするネットワークの範囲を指定
        #target_file = 'nw_scan_results.txt'  # 結果を保存するファイル名を指定
        nm = nmap.PortScanner()
        nm.scan(hosts=target_network, arguments='-sV')

        with open(self.target_file, 'w') as f:
            for host in nm.all_hosts():
                if nm[host].state() == 'up':
                    f.write(f"Host : {host} ({nm[host].hostname()})\n")
                    f.write(f"State : {nm[host].state()}\n")

                    for proto in nm[host].all_protocols():
                        f.write(f"Protocol : {proto}\n")

                        lport = nm[host][proto].keys()
                        sorted_lport = sorted(lport)
                        for port in sorted_lport:
                            service = nm[host][proto][port]
                            f.write(f"port : {port}\tstate : {service['state']}\tservice : {service['name']}\tversion : {service['version']}\n")

                f.write("\n")

    def run(self):
        self.scan_network()

if __name__ == '__main__':
    nw_scan_tool = NwScanTool()
    nw_scan_tool.run()