import subprocess

# LinuxOS ver mod

class LinuxIpChangeTool:
	# ifconfig <interface>
	show_int_cmd = 'ifconfig'
	# ifconfig <interface> <ip> netmask <netmusk> broadcast <broadcast add>
	static_ip_cmd ='sudo ifconfig'
	# ifconfig <interface> dhcp start
	dhcp_cmd = 'sudo ifconfig'
	# sudo ifconfig en0 up/down
	interface_cmd = 'sudo ifconfig'
	
	def show_int(self):
		subprocess.run(self.show_int_cmd, shell=True)
		
	def set_dhcp(self,interface):
		try:
			print(self.dhcp_cmd + ' ' + interface + ' dhcp start')
			subprocess.run(self.dhcp_cmd + ' ' + interface + ' dhcp start', shell=True)
		except:
			print('error : set_dhcp')
	
	def set_ip(self,interface,ipaddress,subnetmask,broadcast_ip):
		try:
			run_static_ip_cmd = self.static_ip_cmd + ' ' + ipaddress + ' netmusk ' + subnetmask + ' broadcast ' + broadcast_ip
			print(run_static_ip_cmd)
			subprocess.run(self.static_ip_cmd,shell=True)
			subprocess.run(self.show_int_cmd + ' ' + interface)
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

[q]: Exit the process
"""
		print(menu_msg)
		
		while True:
			answer = input('Please select a menu : ')
			if answer == '1':
				print("The selected menu is : 1")
				self.show_int()
				network_service = input('Please input network_service : ')
				ip_address = input('Please input ip address : ')
				subnetmask = input('Please input subnetmask : ')
				router_ip = input('Please input router ip address : ')
				self.set_ip(network_service,ip_address,subnetmask,router_ip)
				break
			elif answer == '2':
				print("The selected menu is : 2")
				self.show_int()
				network_service = input('Please input network_service : ')
				interface = input('Please input interface : ')
				self.set_dhcp(network_service)
				self.interface_down(interface)
				self.interface_up(interface)
				break
			elif  answer == 'q':
				print("The selected menu is : 99")
				print("Exited the process.")
				break

if __name__ == "__main__":
	linux_ip_chenge_tool = LinuxIpChangeTool()
	linux_ip_chenge_tool.run()