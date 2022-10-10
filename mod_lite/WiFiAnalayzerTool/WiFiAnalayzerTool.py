import subprocess

class WiFiAnalayzerTool:
  def LinuxWiFiScan(self):
    wifi_scan_all_cmd = 'sh WiFiAnalayzer.sh'
    wifi_scan_wep_cmd = 'sh WiFiAnalayzerWEP.sh'
    menu_text = """/
=== set_sifi_mac menu ===
[1] : wifi scan all
   Scan all access point.

[2] : wifi scan WEP
   Scan for WEP access point.

[q] : quit
=========================
"""
    print(menu_text)

    while True:
      ans = input("select menu number : ")
      if ans == '1':
        subprocess.run(wifi_scan_all_cmd, shell=True)
        break
      elif ans == '2':
        subprocess.run(wifi_scan_wep_cmd, shell=True)
        break
      elif ans == 'q':
        break
      else: 
        print('Enter it again')

  def run(self):
    self.run()

if __name__ == "__main__":
  WiFi_analayzer_tool = WiFiAnalayzerTool()
  pf_result = WiFi_analayzer_tool.run()