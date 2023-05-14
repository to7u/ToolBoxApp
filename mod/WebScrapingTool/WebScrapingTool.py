# -*- coding: utf-8 -*-
# url
from email.quoprimime import header_decode
import requests 
# html perse
from bs4 import BeautifulSoup 
#folder name→day_time
import datetime 
#make dir
import os
#time.sleep
import time
#path error
from urllib.parse import urljoin

class WebScrapingTool:  
	def run(self):
		target_url = input("INPUT URL : ")
		header = {"User-Agent" : "Mozilla/5.0"}
		images = []
		#URL perser
		soup = BeautifulSoup(requests.get(target_url,headers=header).content,'lxml')
		for link in soup.find_all("img"):
			src = urljoin(target_url,link.get("src")) #←←←fix error code
			if "jpg" in src:
				images.append(src)
			elif "png" in src:
				images.append(src)
			elif "gif" in src:
				images.append(src)

		#リストに値がないときメッセージ出力
		if len(images) == 0:
			print("Warning !! Error code !!","[images] has no data")
		else:
			#make folder
			#path = "../../scraping_result/"
			path = "./scraping_result/"
			now = datetime.datetime.now()
			dirname = "img_" + now.strftime("%Y%m%d_%H%M%S")
			#DEBUG
			print(path + dirname)
			os.makedirs(os.path.join(path,dirname),exist_ok=True)

			for link in images:
				ext = os.path.splitext(link)[-1].lower()
				if ext not in ('.jpg', '.jpeg', '.png', '.gif'):
					continue
				re = requests.get(link)
				print("Download:",link)
				with open(os.path.join(path,dirname,link.split("/")[-1]),"wb") as f: 
					f.write(re.content)
					time.sleep(1)

if __name__ == "__main__":
	web_scraping_tool = WebScrapingTool()
	web_scraping_tool.run()