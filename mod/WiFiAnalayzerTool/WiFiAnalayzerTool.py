import subprocess
import platform

class WiFiAnalayzerTool:
  def GetOs(self):
    pf = platform.system()
    print(pf)
    if pf == 'Windows':
      print('on Windows')
    elif pf == 'Darwin':
      print('on Mac')
    elif pf == 'Linux':
      print('on Linux')
    return pf
  
  """
  ■コマンドパス
  /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport

  ■エイリアス登録
  $> alias "airport=/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport" 
  """

  def MacWiFiScan(self):
    menu_text = """/
=== set_sifi_mac menu ===
[1] : wifi on cmd
   PC Wi-Fi ON.

[2] : wifi on cmd
   PC Wi-Fi OFF.
   
[3] : wifi scan all
   Scan all access point.

[4] : wifi scan your ssid
   Scan your access point SSID.

[5] : auto conect SSID
   Auto conect your SSID.

[q] : quit
=========================
"""
    # リアルタイム表示用watchコマンド
    watch_cmd = 'watch'
    # 周囲のWiFiをスキャン
    wifi_scan_all_cmd = 'airport -s'

    # 特定のSSIDを持つWiFiが出力されているか確認
    wifi_scan_ssid_cmd = 'airport -s' # + {my_ssid}

    # 実行時、管理者パスワード必要になる
    # TODO 対象インターフェースはen0固定で問題ないか？
    wifi_on_cmd = 'sudo networksetup -setairportpower en0 on'
    wifi_off_cmd = 'sudo networksetup -setairportpower en0 off'
    wifi_con_cmd = 'sudo networksetup -setairportnetwork en0' # + {my_ssid} {my_pass}

    # WiFiの起動状況を確認
    wifi_status_cmd = 'networksetup -getairportpower en0'
    # 接続中WiFiの詳細情報を取得
    wifi_info_cmd = 'airport -I'
    
    print(menu_text)

    while True:
      ans = input("select menu number : ")
      if ans == '1':
        subprocess.run(wifi_on_cmd, shell=True)
        subprocess.run(wifi_status_cmd, shell=True)
        break
      elif ans == '2':
        subprocess.run(wifi_off_cmd, shell=True)
        subprocess.run(wifi_status_cmd, shell=True)
        break
      elif ans == '3':
        # リアルタイム表示
        print('=== Press Ctrl + c to stop ===')
        subprocess.run(watch_cmd + ' ' + wifi_scan_all_cmd, shell=True)
        break
      elif ans == '4':
        my_ssid = input('Please enter the SSID to set : ')
        subprocess.run(wifi_scan_ssid_cmd + ' ' + my_ssid, shell=True)
        break
      elif ans == '5':
        my_ssid = input('Please enter the SSID to set : ')
        my_pass = input('Please enter the PASS to set : ')
        try:
          subprocess.run(wifi_con_cmd + ' ' + my_ssid + ' ' + my_pass, shell=True)
          subprocess.run(wifi_info_cmd, shell=True)
        except:
          print('WiFi could not be set.')
          subprocess.run(wifi_info_cmd, shell=True)
        break
      elif ans == 'q':
        break
      else:
        print('Enter it again')


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
    pf_result = self.GetOs()

    if pf_result == 'Windows':
      print('Processing for windows is not implemented')
    elif pf_result == 'Darwin':  
      self.MacWiFiScan()
    elif pf_result == 'Linux':
      self.LinuxWiFiScan()

if __name__ == "__main__":
  WiFi_analayzer_tool = WiFiAnalayzerTool()
  pf_result = WiFi_analayzer_tool.GetOs()