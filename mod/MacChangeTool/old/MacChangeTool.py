import subprocess
import re
import os
import netifaces

'''
macchanger未使用パターンスクリプト
'''

class MacChangeTool:
	# クラス変数
	save_path = './'

	def save_default_mac(self,target):
		#デフォルトのinterfaceを別ファイルへ保存(change実行時のみ)→return_macメソッドにて再利用する
		save_file_name = 'default_mac_address_' + target + '.txt'

		if os.path.exists(self.save_path + save_file_name):
			print("The save process was skipped.")
		else:
			print("The save process was executed.")
			interface_address_data = netifaces.ifaddresses(target)
			mac_address   = interface_address_data[netifaces.AF_LINK][0]['addr']
			print("default mac address : " + mac_address)
			f = open(self.save_path + save_file_name, 'w')
			f.write(mac_address)
			f.close()
        
		
	def show_interface(self):
		result_interface = subprocess.run('ifconfig',shell=True)
		print(result_interface)
	
	def select_interface(self):
		interface_name_data = netifaces.interfaces()

		while True:
			target = input('Please select the target interface : ')
			for interface_name in interface_name_data:
				if interface_name == target:
					return target
					break
			print("Please enter the correct interface name.")
	
	# interfaceのdown/upは管理者権でのみ実行可能
	# macchengerコマンドはinterfaceがdownしていると機能しない
	def down_interface(self,target):
		down_cmd = 'ifconfig ' + target + ' down'
		print(down_cmd)
		subprocess.run(down_cmd,shell=True)
		
	def up_interface(self,target):
		up_cmd = 'ifconfig ' + target + ' up'
		print(up_cmd)
		subprocess.run(up_cmd,shell=True)
		
	def change_mac(self,target):
		change_cmd = 'macchanger -r ' + target
		show_cmd = 'macchanger -s ' + target
		print(change_cmd)
		subprocess.run(change_cmd,shell=True)
		subprocess.run(show_cmd,shell=True)
	
	# TODO chenge処理を行なっていないインターフェースを選択するとデフォルトmacファイルがないためエラーになる
	#　save_default_macメソッドで保存した別ファイルから読み込む
	def return_mac(self,target):
		save_file_name = 'default_mac_address_' + target + '.txt'
		show_cmd = 'macchanger -s ' + target
		with open(self.save_path + save_file_name) as f:
			default_mac_address = f.read()
			#print(default_mac_address)
		return_cmd = 'macchanger -m ' + default_mac_address + ' '    + target
		print(return_cmd)
		subprocess.run(return_cmd,shell=True)
		subprocess.run(show_cmd,shell=True)
	
	def run(self):
		# cheange or returnかは選択式で処理を分岐する
		# メニュー選択しを表示
		menu_msg = """
[Mac Changer Controller Menu]

[1] : Change mac address
[2] : Return Mac address

[q] : quit
"""
		print(menu_msg)
		while True:
			answer = input('Please select a menu : ')
			if answer == "1":
				print("The selected menu is : 1")
				self.show_interface()
				target = self.select_interface()
				print("target mac address is : " + target)
				self.save_default_mac(target)
				#self.down_interface(target)
				self.change_mac(target)
				#self.up_interface(target)
				break
			elif answer == "2":
				print("The selected menu is : 2")
				self.show_interface()
				target = self.select_interface()
				print("target interface is : " + target)
				#self.down_interface(target)
				self.return_mac(target)
				#self.up_interface(target)
				break
			elif answer == "q":
				print("The selected menu is : q")
				print("Exited the process.")
				break

if __name__ == "__main__":
	mac_changer_tool = MacChangeTool()
	mac_changer_tool.run()