import subprocess

# MacOS Ver mod

class MacIpChangeTool:
	show_int_cmd = 'networksetup -listnetworkserviceorder'
    
	#sudo /usr/sbin/networksetup -setdhcp Wi-Fi'
	dhcp_cmd = 'sudo /usr/sbin/networksetup -setdhcp'
    
	#sudo /usr/sbin/networksetup -setmanual Wi-Fi 172.xxx.xxx.xxx 255.255.255.0 172.xxx.xxx.xxx'
	static_ip_cmd = 'sudo /usr/sbin/networksetup -setmanual'

	# sudo ifconfig en0 up/down
	interface_cmd = 'sudo ifconfig'
    
	def show_int(self):
		subprocess.run(self.show_int_cmd, shell=True)
    
	def set_dhcp(self,network_service):
		try:
			subprocess.run(self.dhcp_cmd + ' ' + network_service, shell=True)
		except:
			print('error : set_dhcp')
    
	#nw_sv,ip,subnet,router
	def set_ip(self,network_service,ip_address,subnetmask,router_ip):
		try:
			subprocess.run(self.static_ip_cmd + ' ' + network_service + ' ' + ip_address + ' ' + subnetmask + ' ' + router_ip,shell=True)
		except:
			print('error : set_ip')

	def interface_up(self,interface):
		try:
			print(self.interface_cmd + ' ' + interface + ' up')
			subprocess.run(self.interface_cmd + ' ' + interface + ' up',shell=True)
		except:
			print('error : interface_up')

	def interface_down(self,interface):
		try:
			print(self.interface_cmd + ' ' + interface + ' down')
			subprocess.run(self.interface_cmd + ' ' + interface + ' down',shell=True)
		except:
			print('error : interface_down')
	
	def run(self):
		menu_msg = """/
[Mac Changer Controller Menu]

[1] : set static ip address
[2] : set dhcp

[99]: Exit the process
"""
		print(menu_msg)
		
		while True:
			answer = input('Please select a menu : ')
			if answer == '1':
				print("The selected menu is : 1")
				while True:
					self.show_int()
					network_service = input('Please input network_service : ')
					ip_address = input('Please input ip address : ')
					subnetmask = input('Please input subnetmask : ')
					router_ip = input('Please input router ip address : ')
					print(self.static_ip_cmd + ' ' + network_service + ' ' + ip_address + ' ' + subnetmask + ' ' + router_ip)
					print('Do you want to run ? : [y] or [n]')
					print('Cancel processing : [q]')
					exe_answer = input(' : ')
					if exe_answer == 'y':
						self.set_ip(network_service,ip_address,subnetmask,router_ip)
						break
					elif exe_answer == 'q':
						print('Cancel processing')
						break
					else:
						continue
				break
			elif answer == '2':
				print("The selected menu is : 2")
				while True:
					self.show_int()
					network_service = input('Please input network_service : ')
					interface = input('Please input interface : ')
					print(self.dhcp_cmd + ' ' + network_service)
					print('Do you want to run ? : [y] or [n]')
					print('Cancel processing : [q]')
					exe_answer = input(' : ')
					if exe_answer == 'y':
						self.set_dhcp(network_service)
						self.interface_down(interface)
						self.interface_up(interface)
						break
					elif exe_answer == 'q':
						print('Cancel processing')
						break
					else:
						continue
				break
			elif  answer == '99':
				print("The selected menu is : 99")
				print("Exited the process.")
				break

if __name__ == "__main__":
	mac_ip_chenge_tool = MacIpChangeTool()
	mac_ip_chenge_tool.run()